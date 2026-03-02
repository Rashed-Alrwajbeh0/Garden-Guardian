def water_plants(plant_list: list) -> None:
    print("Opening watering system")
    try:
        for plant in plant_list:
            string = "Watering " + plant
            print(string)
    except TypeError:
        print("Error: Cannot water None - invalid plant!")
    finally:
        print("Closing watering system (cleanup)")


def test_watering_system() -> None:
    print("Testing normal watering...")
    water_plants(["tomato", "lettuce", "carrots"])
    print("Watering completed successfully!\n")
    print("Testing with error...")
    water_plants(["tomato", None, "fdfdfdf", 1212])
    print("\nCleanup always happens, even with errors!")


if __name__ == "__main__":
    print("=== Garden Watering System ===\n")
    test_watering_system()
