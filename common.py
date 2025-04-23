inch         = 2.54
dpi          = 72
cm_to_points = dpi / inch

def grayscale_to_hex(value) -> str:
    return f'#{value:02X}{value:02X}{value:02X}'

def decimal_range(start, stop, increment):
    while start < stop:
        yield start
        start += increment

