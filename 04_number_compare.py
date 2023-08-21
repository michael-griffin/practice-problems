def number_compare(a, b):
    """Report on whether a>b, b>a, or b==a

        >>> number_compare(1, 1)
        'Numbers are equal'

        >>> number_compare(-1, 1)
        'Second is greater'

        >>> number_compare(1, -2)
        'First is greater'
    """

    if a > b:
        msg = 'First is greater'
    elif a == b:
        msg = 'Numbers are equal'
    else:
        msg = 'Second is greater'

    return msg

#could return in if/elif