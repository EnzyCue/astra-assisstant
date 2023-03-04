import calendar


def datetime_to_unixepoch(datetime):
    unixepoch = calendar.timegm(datetime.utctimetuple())
    return int(unixepoch)

