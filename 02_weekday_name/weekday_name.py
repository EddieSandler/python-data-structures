def weekday_name(day_of_week):
    """Return name of weekday.

        >>> weekday_name(1)
        'Sunday'

        >>> weekday_name(7)
        'Saturday'

    For days not between 1 and 7, return None

        >>> weekday_name(9)
        >>> weekday_name(0)
    """
# number must be between 1 and 7 (range(1,8))
# create a dict comprehension with num as keys
# create a list of days.
# create list of nums
# iterate through list and insert as dict values

    day = ['Sunday', 'Monday', 'Tuesday',
        'Wednesday', 'Thursday', 'Friday', 'Saturday']
    number = list(range(1, 8))
    result= {number[i]: day[i] for i in range(len(day))}
    if day_of_week in range(1,8):
        return result[day_of_week]
    else:
        return None






