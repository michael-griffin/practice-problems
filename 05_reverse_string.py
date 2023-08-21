def reverse_string(phrase):
    """Reverse string,

        >>> reverse_string('awesome')
        'emosewa'

        >>> reverse_string('sauce')
        'ecuas'
    """
    #W3 way: phrase[::-1]
    reversed = ''
    for ind in range(len(phrase)-1, -1, -1):
        reversed += phrase[ind]

    return reversed
