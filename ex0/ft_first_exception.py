def check_temperature(temp_str: str):
    """
    This function check the temperature and if the temperature is less than 0
    or more than 40 or the temperature not a number it return an Error
    """
    try:
        num = int(temp_str)
        if num < 0:
            print(f"Error: {num}°C is too cold for plants (min 0°C)")
        elif num > 40:
            print(f"Error: {num}°C is too hot for plants (max 40°C)")
        else:
            print(f"Temperature {num}°C is perfect for plants!")
    except ValueError:
        print(f"Error: ’{temp_str}’ is not a valid number")


def test_temperature_input():
    """
    This function test a different cases
    """
    print("Testing temperature: 25")
    check_temperature("25")
    print("\nTesting temperature: abc")
    check_temperature("abc")
    print("\nTesting temperature: 100")
    check_temperature("100")
    print("\nTesting temperature: -50")
    check_temperature("-50")
    print("\nAll tests completed - program didn’t crash!")


if __name__ == "__main__":
    print("=== Garden Temperature Checker ===\n")
    test_temperature_input()
