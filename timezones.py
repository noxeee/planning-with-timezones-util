from datetime import timezone, datetime
import sys
import pytz


def parsetime(time: str):
    return datetime.strptime(time, '%Y-%m-%dT%H:%M:%S.%f%z')


def printtimes(locs: list[str], time: datetime):

    fmt = '%Y-%m-%d %H:%M:%S %Z%z'

    for tz in locs:
        localdt = time.astimezone(pytz.timezone(tz))
        print(localdt.strftime(fmt), tz)


if __name__ == '__main__':

    nowtime = datetime.now(timezone.utc)

    locations = ['America/Los_Angeles', 'America/Denver',
                 'America/New_York', 'Europe/London', 'Europe/Vienna',
                 'Europe/Istanbul', 'Australia/Melbourne']

    print(f"Time entered: {nowtime} in {nowtime.tzname()}")

    if len(sys.argv) > 1:
        nowtime = parsetime(sys.argv[1])

    printtimes(locations, nowtime)