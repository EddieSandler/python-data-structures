def mode(nums):
    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of times.

        >>> mode([1, 2, 1])
        1

        >>> mode([2, 2, 3, 3, 2])
        2
    """

    my_dict={num:nums.count(num) for num in nums}
    the_max =max(my_dict.values())
    for key in my_dict.keys():
        if my_dict[key] == the_max:
            return key