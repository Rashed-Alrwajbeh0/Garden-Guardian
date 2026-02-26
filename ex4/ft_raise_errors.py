def check_plant_health(plant_name, water_level, sunlight_hours):
    """
    This function check if the plant_name is not empty and if the
    water level is between 1 and 10 and if the sunlight hours is
    betweeb 2 and 12
    """
    all_done = 1
    try:
        if plant_name == "":
            raise ValueError("Error: Plant name cannot be empty!")
    except ValueError as e:
        print(e)
        all_done = 0
    try:
        if water_level > 10:
            raise ValueError(f"Error: Water level {water_level} "
                             "is too high (max 10)")
        elif water_level < 1:
            raise ValueError(f"Error: Water level {water_level} "
                             "is too low (min 1)")
    except ValueError as e:
        print(e)
        all_done = 0
    try:
        if sunlight_hours < 2:
            raise ValueError(f"Error: Sunlight hours {sunlight_hours} "
                             "is too low (min 2)")
        elif sunlight_hours > 12:
            raise ValueError(f"Error: Sunlight hours {sunlight_hours} "
                             "is too high (max 12)")
    except ValueError as e:
        print(e)
        all_done = 0
    if all_done == 1:
        print(f"Plant ’{plant_name}’ is healthy!")


def test_plant_checks():
    """
    Test a different cases
    """
    print("Testing good values...")
    check_plant_health("tomato", 5, 5)
    print("\nTesting empty plant name...")
    check_plant_health("", 5, 5)
    print("\nTesting bad water level...")
    check_plant_health("tomato", 15, 10)
    print("\nTesting bad sunlight hours...")
    check_plant_health("tomato", 1, 0)
    print("\nAll error raising tests completed!")


if __name__ == "__main__":
    print("=== Garden Plant Health Checker ===\n")
    test_plant_checks()
