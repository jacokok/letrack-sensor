import uasyncio
from machine import Pin
from utime import ticks_ms
from event import Event


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

    async def check(self):
        if self.event.id != self.prev_event.id:
            self.prev_event = self.event
            uasyncio.create_task(self.publish_event(self.event))

    async def publish_event(self, event: Event):
        print("publish event to mqtt here", event)
        self.led.on()
        await uasyncio.sleep_ms(1000)
        self.led.off()
