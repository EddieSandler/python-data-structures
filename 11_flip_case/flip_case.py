def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    # letters = [char for char in phrase]
    # result =[]

    # for char in letters:
    #     if char == to_swap.lower():
    #         char = char.upper()
    #         result.append(char)

    #     elif char == to_swap.upper():
    #         char = char.lower()
    #         result.append(char)
    #     else:
    #         result.append(char)


    # return ''.join(result)




    result = [
                char.upper() if char == to_swap.lower()
                else char.lower() if char == to_swap.upper()
                else char for char in phrase
            ]
    return ''.join(result)