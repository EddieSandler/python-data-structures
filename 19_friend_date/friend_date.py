def friend_date(a, b):
    """Given two friends, do they have any hobbies in common?

    - a: friend #1, a tuple of (name, age, list-of-hobbies)
    - b: same, for friend #2

    Returns True if they have any hobbies in common, False is not.

        >>> elmo = ('Elmo', 5, ['hugging', 'being nice'])
        >>> sauron = ('Sauron', 5000, ['killing hobbits', 'chess'])
        >>> gandalf = ('Gandalf', 10000, ['waving wands', 'chess'])

        >>> friend_date(elmo, sauron)
        False

        >>> friend_date(sauron, gandalf)
        True
    """
    #slice off list , create sets of all elements, find common elements between joined sets
    name_age_1=set(a[:2])
    hobby_1= set(a[-1])


    name_age_2=set(b[:2])
    hobby_2=set(b[-1])

    if len((name_age_1 | hobby_1) & (name_age_2| hobby_2)) >0:
        return True
    return False


