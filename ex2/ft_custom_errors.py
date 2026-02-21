class GardenError(Exception):
    """
    This class to make a garden error
    """
    def __init__(self, message: str):
        super().__init__(message)
        self.message = message

    def print_error(self):
        print("Caught a garden error:", self.message)


class PlantError(GardenError):
    """
    This class to make a plant error
    """
    def __init__(self, message2: str, message1: str = None):
        super().__init__(message1)
        self.message2 = message2

    def print_error(self):
        print("Caught PlantError:", self.message2)


class WaterError(GardenError):
    """
    This class to make a water error
    """
    def __init__(self, message2: str, message1: str = None):
        super().__init__(message1)
        self.message2 = message2

    def print_error(self):
        print("Caught WaterError:", self.message2)


def testing():
    """
    This function test a different cases
    """
    try:
        print("Testing PlantError...")
        raise PlantError("The tomato plant is wilting!")
    except PlantError as e:
        e.print_error()
    print()
    try:
        print("Testing WaterError...")
        raise WaterError("Not enough water in the tank!")
    except WaterError as e:
        e.print_error()
    print()
    try:
        print("Testing catching all garden errors...")
        raise GardenError("The tomato plant is wilting!")
    except GardenError as e:
        e.print_error()
    try:
        raise GardenError("Not enough water in the tank!")
    except GardenError as e:
        e.print_error()
    print("\nAll custom error types work correctly!\n")


if __name__ == "__main__":
    print("=== Custom Garden Errors Demo ===\n")
    testing()
