def single_letter_count(word, letter):
    """How many times does letter appear in word (case-insensitively)?

        >>> single_letter_count('Hello World', 'h')
        1

        >>> single_letter_count('Hello World', 'z')
        0

        >>> single_letter_count("Hello World", 'l')
        3
    """
    count1=0
    count2=0
    count1 = word.count(letter.lower())
    count2 = word.count(letter.upper())

    return count1+count2
