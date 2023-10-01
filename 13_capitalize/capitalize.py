def capitalize(phrase):
    """Capitalize first letter of first word of phrase.

        >>> capitalize('python')
        'Python'

        >>> capitalize('only first word')
        'Only first word'
    """
    # letters=[letter for letter in phrase]
    # letters[0]=letters[0].upper()
    # return ''.join(letters)

    return phrase[0].upper()+ phrase[1:]
