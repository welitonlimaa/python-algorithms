def study_schedule(permanence_period, target_time):
    if target_time is None:
        return None
    count = 0
    for period in permanence_period:
        if (
            not (isinstance(period, tuple)) or
            not (isinstance(period[0], int)) or
            not (isinstance(period[1], int))
        ):
            return None
        if target_time >= period[0] and target_time <= period[1]:
            count += 1
    return count


periods = [(2, 2), (1, 2), (2, 3), (1, 5), (4, 5), (4, 5)]

print(study_schedule(periods, 5))
