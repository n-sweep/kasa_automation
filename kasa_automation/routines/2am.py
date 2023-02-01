#!/usr/bin/env python3
# 2am routine

import asyncio
from crontab import CronTab
from src.lights import DeviceHandler
from src.weather import get_sunset

ms_20m = 1000 * 60 * 20

devices_delayed = [
    'front porch light',
    'front yard light'
]

devices_immediate = [
    'office light a',
]


async def lights():
    dh = DeviceHandler()
    await dh._init()

    for dev_name in devices_delayed:
        dev = await dh.get_device_by_name(dev_name)
        await dev.turn_off(transition=ms_20m)

    for dev_name in devices_immediate:
        dev = await dh.get_device_by_name(dev_name)
        await dev.turn_off()


def get_cron_job(ct, comment='', command=''):
    if comment:
        jobs = list(ct.find_comment(comment))
        if jobs:
            return jobs[0]

    if command:
        jobs = list(ct.find_command(command))
        if jobs:
            return jobs[0]

    return None


def cron_2am(ct):
    comment = 'routine 2am'
    command = 'python /usr/bin/ka 2am'

    job = get_cron_job(ct, comment)
    if not job:
        job = ct.new(comment=comment, command=command)
        job.minute.on(0)
        job.hour.on(2)


def cron_sunset(ct):
    comment = 'routine sunset'
    command = 'python /usr/bin/ka sunset'

    job = get_cron_job(ct, comment)
    if not job:
        job = ct.new(comment=comment, command=command)

    min, hr = get_sunset()
    job.minute.on(min)
    job.hour.on(hr)


def cron():
    with CronTab(user='n') as ct:
        # make sure the 2am routine cron job exists
        cron_2am(ct)
        # reset sunset cronjob
        cron_sunset(ct)


def routine():
    # cron routines
    cron()
    # turn off lights
    asyncio.run(lights())



if __name__ == "__main__":
    routine()
