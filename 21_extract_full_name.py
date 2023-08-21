def extract_full_names(people):
    """Return list of names, extracting from first+last keys in people dicts.

    - people: list of dictionaries, each with 'first' and 'last' keys for
              first and last names

    Returns list of space-separated first and last names.

        >>> names = [
        ...     {'first': 'Ada', 'last': 'Lovelace'},
        ...     {'first': 'Grace', 'last': 'Hopper'},
        ... ]

        >>> extract_full_names(names)
        ['Ada Lovelace', 'Grace Hopper']
    """
    #first_names = [val for person in people for (key,val) in person.items() if key == 'first']
    first_names = [person['first'] for person in people]
    last_names = [person['last'] for person in people]

    full_names = []
    #for loop to combine
    for ind in range(len(first_names)):
        full_names.append(f"{first_names[ind]} {last_names[ind]}")

    return full_names


people = [ {'first': 'Ada', 'last': 'Lovelace'},  {'first': 'Grace', 'last': 'Hopper'}]