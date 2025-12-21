def safe_call(func, a, b):
    ### Replace with your own code (begin) ###
    try:
        result = func (a, b)
        return (True, result, None)
    except (ZeroDivisionError, TypeError, ValueError, IndexError, KeyError) as e:
        return (False, None, type(e).__name__)
    ### Replace with your own code (end)   ###
