def last_element(lst):
    """Return last item in list (None if list is empty.

        >>> nums = [1, 2, 3]
        >>> last_element(nums)
        3
        >>> last_element([]) is None
        True

    Make sure original list has not been mutated:

        >>> nums == [1, 2, 3]
        True
    """
    if len(lst):
        return lst[len(lst)-1]
    else:
        return None

    #don't return none, don't need to check if list has length of 0
