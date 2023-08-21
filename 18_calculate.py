def calculate(operation, a, b, make_int=False, message='The result is'):
    """Perform operation on a + b, ()possibly truncating) & returning w/msg.

    - operation: 'add', 'subtract', 'multiply', or 'divide'
    - a and b: values to operate on
    - make_int: (optional, defaults to False) if True, truncates to integer
    - message: (optional) message to use (if not provided, use 'The result is')

    Performs math operation (truncating if make_int), then returns as
    "[message] [result]"

        >>> calculate('add', 2.5, 4)
        'The result is 6.5'

        >>> calculate('subtract', 4, 1.5, make_int=True)
        'The result is 2'

        >>> calculate('multiply', 1.5, 2)
        'The result is 3.0'

        >>> calculate('divide', 10, 4, message='I got')
        'I got 2.5'

    If a valid operation isn't provided, raise error:

        >>> calculate('foo', 2, 3)
        Traceback (most recent call last):
          ...
        ValueError: Invalid Operation
    """
    #operation: 'add', 'subtract', 'multiply', or 'divide'
    operators = {'add', 'subtract', 'multiply', 'divide'}

    #num_result
    if operation not in operators:
        raise ValueError('Invalid Operation')
    else:
        if operation == "add":
            result = a + b
        elif operation == "subtract":
            result = a - b
        elif operation == "multiply":
            result = a * b
        else: #division, make explicit
            result = a / b
    #take result, makeInt
    if make_int:
        result = round(result)

    #return final message
    return f"{message} {result}"
    #final form is f"{msg} {num}"