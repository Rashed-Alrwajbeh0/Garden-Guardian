def garden_operations(e: type) -> None:
    if e == ValueError:
        for c in 'abc':
            if c > '9' or c < '0':
                raise ValueError('invalid literal for int()')
    elif e == ZeroDivisionError:
        print(1/0)
    elif e == FileNotFoundError:
        file = open("missing.txt", "r")
        file.close()
    elif e == KeyError:
        dictionary = {
            "name": "Rashed",
            "age": 18
                }
        print(dictionary["missing_plant"])


def test_error_types() -> None:
    try:
        print("Testing ValueError...")
        garden_operations(ValueError)
    except ValueError:
        print("Caught ValueError: invalid literal for int()")
    try:
        print("\nTesting ZeroDivisionError...")
        garden_operations(ZeroDivisionError)
    except ZeroDivisionError:
        print("Caught ZeroDivisionError: division by zero")
    try:
        print("\nTesting FileNotFoundError...")
        garden_operations(FileNotFoundError)
    except FileNotFoundError:
        print("Caught FileNotFoundError: No such file ’missing.txt’")
    try:
        print("\nTesting KeyError...")
        garden_operations(KeyError)
    except KeyError:
        print("Caught KeyError: ’missing_plant’")
    try:
        print("\nTesting multiple errors together...")
        garden_operations(ZeroDivisionError)
    except (ValueError, ZeroDivisionError, FileNotFoundError, KeyError):
        print("Caught an error, but program continues!")
    print("\nAll error types tested successfully!")


if __name__ == "__main__":
    print("=== Garden Error Types Demo ===\n")
    test_error_types()
