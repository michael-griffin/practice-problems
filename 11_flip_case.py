def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    #check string methods for how to swap cases easier
    swapped_str = ""
    for letter in phrase:
        if to_swap.lower() == letter:
            swapped_str += to_swap.upper()
        elif to_swap.upper() == letter:
            swapped_str += to_swap.lower()
        else:
            swapped_str += letter

    return swapped_str