import common

w = 0
h = 0

def draw_vertical_line(c, x):
    c.line(x, 0, x, h)

def draw_horizontal_line(c, y):
    c.line(0, y, w, y)

def draw_lines(c, limit, interval, color, skip, func):
    c.setStrokeColor(color)
    i = -1;
    for x in common.decimal_range(0, limit, interval):
        i += 1
        if skip != 0 and i % skip == 0:
            continue
        func(c, x)

def draw(canvas, page_width, page_height):
    global w, h

    w = page_width
    h = page_height

    line_color_1mm          = common.grayscale_to_hex(240)
    line_color_5mm          = common.grayscale_to_hex(230)
    line_color_1cm          = common.grayscale_to_hex(220)

    line_spacing_1mm        = 0.1 * common.cm_to_points
    line_spacing_5mm        = 0.5 * common.cm_to_points
    line_spacing_1cm        = 1.0 * common.cm_to_points

    draw_lines(canvas, h, line_spacing_1mm, line_color_1mm, 5, draw_horizontal_line)
    draw_lines(canvas, w, line_spacing_1mm, line_color_1mm, 5, draw_vertical_line  )

    draw_lines(canvas, h, line_spacing_5mm, line_color_5mm, 0, draw_horizontal_line)
    draw_lines(canvas, w, line_spacing_5mm, line_color_5mm, 0, draw_vertical_line  )

    draw_lines(canvas, h, line_spacing_1cm, line_color_1cm, 0, draw_horizontal_line)
    draw_lines(canvas, w, line_spacing_1cm, line_color_1cm, 0, draw_vertical_line  )

