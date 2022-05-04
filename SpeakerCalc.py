import math


def get_length() -> float:
    length = float(input("Enter room length: "))
    return length


def get_width() -> float:
    width = float(input("Enter room width: "))
    return width


def get_height() -> float:
    height = float(input("Enter mounted speaker height AFF: "))
    return height


def get_ear_height() -> float:
    ear = float(input("Enter listener height (eg 4 = seated, 6 = standing): "))
    return ear


def get_dispersion() -> float:
    dispersion = float(input("Enter speaker dispersion angle: "))
    return dispersion


def calc_sqft(length: float, width: float) -> float:
    area = length * width
    print("Your room's total area: ", area)
    print()
    return area


def calc_spkr_cone(dispersion: float, height: float, ear: float) -> float:
    """
        calculates the dispersion cone
        returning its diameter
    """
    radian = math.radians(dispersion)
    diameter = (2 * (height - ear)) * (math.tan(radian / 2))
    print("\nThe diamter of your speaker cone at listener height: ", diameter)
    return diameter


def get_spkr_area(diameter: float) -> float:
    radius = diameter / 2
    area = 3.14 * (radius * radius)
    print("Area of speaker cone: ", area)
    return area


def spacing(diameter: float):
    radius = diameter / 2
    distance = 2 * radius
    min_overlap = radius * math.sqrt(2)
    print()
    print("Edge-To-Edge: ", distance)
    print("Minimum overlap: ", min_overlap)
    print("Center-To-Center: ", radius)


def speaker_count(room_area: float, spkr_area: float) -> float:
    count = math.ceil((room_area / spkr_area))
    print("Estimated number of speakers required: ", count)
    return count


def main():
    print("This calculator ignores your unit of mesaure.")
    print("You must enter values as decimals eg 10.5")
    length = get_length()
    width = get_width()
    height = get_height()
    room_area = calc_sqft(length, width)
    ear = get_ear_height()
    dispersion = get_dispersion()
    diameter = calc_spkr_cone(dispersion, height, ear)
    spkr_area = get_spkr_area(diameter)
    spacing(diameter)
    speaker_count(room_area, spkr_area)

if __name__ == "__main__":
    main()
