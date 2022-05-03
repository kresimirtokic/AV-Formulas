import math


def get_horiz() -> int:
    """ function gets and returns horizontal resolution input from user """
    horiz = int(input("Enter Horizontal Resolution: "))
    return horiz


def get_vert() -> int:
    """ function gets and returns vertical resolution input from user """
    vert = int(input("Enter Vertical Resolution: "))
    return vert


def get_fps() -> int:
    """ function gets and returns refresh/fps input from user """
    fps = int(input("Enter Refresh/FPS Rate: "))
    return fps


def get_bit() -> int:
    """ function gets and returns color bit depth input from user """
    bit = int(input("Enter Color Bit Depth: "))
    # bits_per_pixel = bit * 3
    return bit


def bytes_per_pixel(bits: int, sample_rate: int) -> float:
    """ function returns bytes per pixel """
    bpp = (bits * 3) / sample_rate
    return bpp


def get_chroma() -> list:
    """ function gets and returns chroma sampling input from user
    and divisor as appropriate for chroma sub sampling """
    chromaR = int(input("Enter Chroma Sample Red: "))
    chromaG = int(input("Enter Chroma Sample Green: "))
    chromaB = int(input("Enter Chroma Sample Blue: "))
    chroma = [chromaR, chromaG, chromaB]
    if (chromaR == 4):
        if (chromaG == 4):
            if (chromaB == 4):
                chroma.append(1)
        if (chromaG == 2):
            if (chromaB == 2):
                chroma.append(1.5)
            if (chromaB == 0):
                chroma.append(2)
    return chroma


def get_bandwidth(horiz: int, vert: int, fps: int,
                  bits_per_pixel: float) -> float:
    """ function returns bandwidth """
    bandwidth = horiz * vert * fps * bits_per_pixel
    return bandwidth


def get_gb(bandwidth: float) -> float:
    """ function returns bandwidth as gigabyte """
    # mb = bandwidth/(1024*1024)
    # gb = bandwidth / ( 1024 * 1024 * 1024)
    gb = bandwidth / (1000 * 1000 * 1000)
    return round(gb, 1)


def get_encoders() -> int:
    """ function gets total quantity of encoders from user input """
    qty = int(input("Enter Total Number of Encoders: "))
    return qty


def total_bandwidth(bandwidth: float, qty: int) -> float:
    """ function returns total bandwidth required for all encoders """
    total = bandwidth * qty
    return total


def display_start():
    """ function displays start text """
    print()
    print(60*'*')
    print('** This determines the bandwidth of AVoIP video encoders  **')
    print(60*'*')
    print()
    return 0


def display_results(horiz, vert, fps, bit, chroma, bandwidth, total):
    """ function displays results on screen """
    chroma.reverse()
    print()
    print(70*'*')
    print('* Bandwidth of ', horiz, 'x', vert, ' @', fps, 'fps ', bit,
          '-bit color & chroma sampling-', chroma.pop(2), ':',
          chroma.pop(1), ':', chroma.pop(0), '  *', sep='')
    print(70*'*')
    print(' ', bandwidth, 'bps per encoder')
    print(' ', get_gb(bandwidth), 'Gbps per encoder')
    print(70*'*')
    print(' ', total, 'bps system total')
    print(' ', get_gb(total), 'Gbps system total')
    print(70*'*')
    print()
    return 0


def main():
    # call display stuff
    display_start()

    # this block gets user input saves to vars
    horiz = get_horiz()
    vert = get_vert()
    fps = get_fps()
    bit = get_bit()
    chroma = get_chroma()
    bpp = bytes_per_pixel(bit, chroma.pop(3))
    bandwidth = get_bandwidth(horiz, vert, fps, bpp)
    qty = get_encoders()
    total = total_bandwidth(bandwidth, qty)

    # show the results
    display_results(horiz, vert, fps, bit, chroma, bandwidth, total)

if __name__ == "__main__":
    main()
