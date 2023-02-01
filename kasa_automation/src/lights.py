#!/usr/bin/env python3
# Kasa automation

import asyncio
from kasa import Discover


async def print_alias(device):
    onoff = ' ON' if device.is_on else 'OFF'
    print(f'Discovered [{onoff}] {device.alias}')


class DeviceHandler:
    async def _init(self):
        await self.refresh_devices()

    async def refresh_devices(self):
        found = await Discover.discover()
        self.devices = {d.alias: d for d in found.values()}

    async def get_device_by_name(self, name):
        for i in range(3):
            if name in self.devices:
                return self.devices[name]
            elif i < 2:
                print(f'{name} not found, refreshing devices...')
                await self.refresh_devices()

        keys = list(devices.keys())
        print(f'No device named {name} found. Devices found: {keys}')

        return []

    async def device(self, name):
        return await self.get_device_by_name(name)


async def main():
    dh = DeviceHandler()
    await dh._init()

    o = await dh.device('office light a')
    await o.turn_off(transition=10000)

if __name__ == '__main__':
    asyncio.run(main())
