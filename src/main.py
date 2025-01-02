import uasyncio
from machine import Pin
from track import BreakBeam


async def beam_handler(beam: BreakBeam):
    while True:
        uasyncio.create_task(beam.check())
        await uasyncio.sleep_ms(0)


async def main():
    beam1 = Pin(10, Pin.IN, Pin.PULL_UP)
    beam2 = Pin(12, Pin.IN, Pin.PULL_UP)
    bb1 = BreakBeam(beam1, 1)
    bb2 = BreakBeam(beam2, 2)
    while True:
        uasyncio.create_task(beam_handler(bb1))
        uasyncio.create_task(beam_handler(bb2))
        await uasyncio.sleep(10_000)


uasyncio.run(main())
