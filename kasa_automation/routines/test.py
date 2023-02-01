#!/usr/bin/env python3
# sunset routine

import asyncio
from src.lights import DeviceHandler

ms_5m = 1000 * 60 * 5

async def lights():
    dh = DeviceHandler()
    await dh._init()

    dev = await dh.get_device_by_name('office light a')
    await dev.set_brightness(30, transition=ms_5m)


def routine():
    asyncio.run(lights())


if __name__ == "__main__":
    routine()
