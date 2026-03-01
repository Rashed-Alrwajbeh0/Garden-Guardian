def check_temperature(temp_str: str) -> None | int:
    try:
        num: int = int(temp_str)
        if num < 0:
            print(f"Error: {num}°C is too cold for plants (min 0°C)")
            return None
        elif num > 40:
            print(f"Error: {num}°C is too hot for plants (max 40°C)")
            return None
        else:
            print(f"Temperature {num}°C is perfect for plants!")
            return num
    except ValueError:
        print(f"Error: ’{temp_str}’ is not a valid number")
        return None


def test_temperature_input() -> None:
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
