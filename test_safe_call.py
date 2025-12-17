from safe_call import safe_call

def test_safe_call_success():
    def add(a, b):
        return a + b

    ok, value, error = safe_call(add, 2, 3)

    assert ok is True
    assert value == 5
    assert error is None


def test_safe_call_zero_division():
    def divide(a, b):
        return a / b

    ok, value, error = safe_call(divide, 10, 0)

    assert ok is False
    assert value is None
    assert error == "ZeroDivisionError"
