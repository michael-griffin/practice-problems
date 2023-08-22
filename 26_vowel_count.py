def vowel_count(phrase):
    """Return frequency map of vowels, case-insensitive.

        >>> vowel_count('rithm school')
        {'i': 1, 'o': 2}

        >>> vowel_count('HOW ARE YOU? i am great!')
        {'o': 2, 'a': 3, 'e': 2, 'u': 1, 'i': 1}
    """
    phrase_low = phrase.lower()

    #make a frequency counter
    counter = {}
    vowels = 'aeiou'
    for char in phrase_low:

        if char in vowels:
            counter[char] = counter[char] +1 if (counter.get(char)) else 1
            # if counter.get(char):
            #     counter[char] += 1
            # else:
            #     counter[char] = 1

    return counter