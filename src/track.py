import uasyncio
from machine import Pin
from utime import ticks_ms, time_ns, gmtime
from event import Event
from umqtt.robust import MQTTClient
import json
import config


class BreakBeam:
    def __init__(self, beam: Pin, trackId: int):
        self.beam = beam
        self.time = ticks_ms()
        event = Event(trackId)
        self.event = event
        self.prev_event = event
        self.trackId = trackId
        self.led = Pin("LED", Pin.OUT)

        self.beam.irq(
            handler=self.break_handler,
            trigger=Pin.IRQ_FALLING | Pin.IRQ_RISING,
        )

    def break_handler(self, pin: Pin):
        diff = ticks_ms() - self.time
        if diff > 500:
            self.time = ticks_ms()
            self.event = Event(self.trackId)

    async def check(self, mqtt: MQTTClient):
        if self.event.id != self.prev_event.id:
            self.prev_event = self.event
            uasyncio.create_task(self.publish_event(self.event, mqtt))

    async def publish_event(self, event: Event, mqtt: MQTTClient):
        current_ns = time_ns()
        utc_string = utc_from_ns(current_ns)
        print("publish event to mqtt here", event)
        event_json = json.dumps(
            {
                "Id": event.id.__str__(),
                "TrackId": event.trackId,
                "Timestamp": utc_string,
            }
        )
        mqtt.publish("event", event_json)
        self.led.on()
        await uasyncio.sleep_ms(1000)
        self.led.off()


def utc_from_ns(ns):
    try:
        seconds = ns // 1000000000
        nanoseconds = ns % 1000000000
        # Timezone offset fix
        tm = gmtime(seconds + (-1 * config.TZ_OFFSET * 3600))

        # Format the string, including fractional seconds
        return "{:04d}-{:02d}-{:02d}T{:02d}:{:02d}:{:02d}.{:06d}Z".format(
            tm[0],
            tm[1],
            tm[2],
            tm[3],
            tm[4],
            tm[5],
            nanoseconds // 1000,  # microseconds
        )
    except OverflowError:
        print("OverflowError: Nanoseconds value is too large.")
        return None
    except Exception as e:  # catch other exceptions
        print(f"An error occurred: {e}")
        return None
