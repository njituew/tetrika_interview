def strict(func):
    def wrapper(*args, **kwargs):
        annotations = func.__annotations__

        # check args
        for i, arg in enumerate(args):
            param_name = list(annotations.keys())[i]
            expected_type = annotations.get(param_name)

            if expected_type and not isinstance(arg, expected_type):
                raise TypeError(
                    f"Argument {param_name} expected {expected_type}, got {type(arg)} instead."
                )

        # check kwargs
        for param_name, arg in kwargs.items():
            expected_type = annotations.get(param_name)

            if expected_type and not isinstance(arg, expected_type):
                raise TypeError(
                    f"Argument {param_name} expected {expected_type}, got {type(arg)} instead."
                )

        return func(*args, **kwargs)

    return wrapper

@strict
def sum_two(a: int, b: int) -> int:
    return a + b


if __name__ == "__main__":
    print(sum_two(1, 2))
    # print(sum_two(1, "sad"))