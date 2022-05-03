def get_watts() -> float:
    """ function gets user input for watts per device """
    watts = float(input("Enter watts for this device: "))
    if watts >= 30:
        print('Note: You will need PoE++ to support this device')
    if watts > 15.5 and watts < 30:
        print('Note: You will need PoE+ to support this device')
    return watts


def get_device_count() -> int:
    """ function gets user input for total number of devices """
    total = int(input("Enter total number of PoE devices: "))
    return total


def main():
    device_count = get_device_count()
    i = 0
    total_watts = 0
    while (i < device_count):
        watts = get_watts()
        total_watts += watts
        i += 1
    print('Total PoE budget required:', total_watts)


if __name__ == "__main__":
    main()
