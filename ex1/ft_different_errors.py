def garden_operations(e):
    """
    This function generate error cases
    """
    if e == ValueError:
        print(int("abc"))
    elif e == ZeroDivisionError:
        print(1/0)
    elif e == FileNotFoundError:
        file = open("test.txt", "r")
        file.close()
    elif e == KeyError:
        dictionary = {
            "name": "Rashed",
            "age": 18
                }
        print(dictionary["Name"])


def test_error_types():
    """
    This function test a different cases
    """
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
