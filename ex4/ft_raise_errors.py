class GardenError(Exception): 
    pass


class PlantError(GardenError): 
    pass


class WaterError(GardenError): 
    pass


def check_plant_health(plant_name: str, water_level: int,
                       sunlight_hours: int) -> None:
    all_done: int = 1
    try:
        if plant_name == "":
            raise GardenError("Error: Plant name cannot be empty!")

        if water_level > 10:
            raise WaterError(f"Error: Water level {water_level}" 
                             " is too high (max 10)")
        elif water_level < 1:
            raise WaterError(f"Error: Water level {water_level}"
                             " is too low (min 1)")
        if sunlight_hours < 2:
            raise PlantError(f"Error: Sunlight hours {sunlight_hours}"
                             " is too low (min 2)")
        elif sunlight_hours > 12:
            raise PlantError(f"Error: Sunlight hours {sunlight_hours}"
                             " is too high (max 12)")

    except (GardenError, WaterError, PlantError) as e:
        print(e)
        all_done = 0

    if all_done == 1:
        print(f"Plant '{plant_name}' is healthy!")

def test_plant_checks() -> None:
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
