def multiple_letter_count(phrase):
    """Return dict of {ltr: frequency} from phrase.

        >>> multiple_letter_count('yay')
        {'y': 2, 'a': 1}

        >>> multiple_letter_count('Yay')
        {'Y': 1, 'a': 1, 'y': 1}
    """
    #frequency counter from lecture
    counter = {}
    for letter in phrase:
        counter[letter] = counter[letter] + 1 if letter in counter else 1

    return counter

#use or operator
