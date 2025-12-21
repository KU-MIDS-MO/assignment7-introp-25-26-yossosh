def build_pipeline(operation_names):
    ### Replace with your own code (begin) ###
    ops = {
        "double": lambda x: 2 * x,
        "triple": lambda x: 3 * x,
        "square": lambda x: x * x,
        "add1": lambda x: x + 1,
        "sub1": lambda x: x - 1,
        "negate": lambda x: -x
    }

    if not isinstance(operation_names, list):
        raise TypeError("operation_names must be a list")

    for name in operation_names:
        if not isinstance(name, str):
            raise TypeError("each operation name must be a string")
        if name not in ops:
            raise KeyError(name)   # <- важливо для тесту

    pipeline_ops = [ops[name] for name in operation_names]

    def apply_operations(x):
        for operation in pipeline_ops:
            x = operation(x)
        return x

    return apply_operations
    ### Replace with your own code (end)   ###
p = build_pipeline(["double", "square"])
p(10)
