def study_schedule(permanence_period, target_time):
    counter = 0
    if target_time is None or target_time < 0:
        return None
    for period in permanence_period:
        if type(period[0]) is not int or type(period[1]) is not int:
            return None
        if int(period[0]) <= int(target_time) <= int(period[1]):
            counter += 1
    return counter
