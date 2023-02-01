#!/usr/bin/env python3
# sunset routine

import asyncio
from src.lights import DeviceHandler

ms_hour = 1000 * 60 * 60
devices = ['front porch light', 'front yard light']


async def lights():
    dh = DeviceHandler()
    await dh._init()

    for dev_name in devices:
        dev = await dh.get_device_by_name(dev_name)
        await dev.set_brightness(100, transition=ms_hour)


def routine():
    asyncio.run(lights())


if __name__ == "__main__":
    routine()
