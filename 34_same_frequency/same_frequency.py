def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?

        >>> same_frequency(551122, 221515)
        True

        >>> same_frequency(321142, 3212215)
        False

        >>> same_frequency(1212, 2211)
        True
    """
    digit1,digit2 =str(num1),str(num2)
    new_num1=sort_nums(digit1)
    new_num2=sort_nums(digit2)
    return new_num1== new_num2

def sort_nums(x):
    digits=[char for char in x]
    return''.join(sorted(digits))
















#''.join(sorted(input_string))