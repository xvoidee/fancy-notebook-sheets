import common

def draw(canvas, page_width, page_height):
    dot_color    = common.grayscale_to_hex(220)
    dot_spacing  = 0.5 * common.cm_to_points
    dot_radius   = 0.5

    canvas.setStrokeColor(dot_color)
    canvas.setFillColor  (dot_color)

    for y in common.decimal_range(0, page_height, dot_spacing):
        for x in common.decimal_range(0, page_width, dot_spacing):
            canvas.circle(x, y, dot_radius)

