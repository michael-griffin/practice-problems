def titleize(phrase):
    """Return phrase in title case (each word capitalized).

        >>> titleize('this is awesome')
        'This Is Awesome'

        >>> titleize('oNLy cAPITALIZe fIRSt')
        'Only Capitalize First'
    """
    #lowercase phrase, split on spaces, then use .capitalize()
    phrase_low = phrase.lower()
    words = phrase_low.split(' ')



    title_words = [word.capitalize() for word in words]
    return ' '.join(title_words)

    # formatted = ''
    # for word in words:
    #     formatted += word.capitalize() + ' '

    ##join back at end

    #title() method