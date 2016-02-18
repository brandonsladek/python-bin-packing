
# Brandon Sladek and Alex Calderwood

""" Strategy:
    
    Sort through, put in dictionary based on width range
    Place in even-width columns (based on max-width of the range) in bin
    Re-place boxes from left to right when boxes from left can be put in columns to right since the next column to the right is guaranteed to hold boxes with larger width

"""

"""
FIND_SOLUTION:
    Define this function in BinPacking.py, along with any auxiliary
functions that you need.  Do not change the Driver.py file at all.
--------------------------------------------------
rectangles: a list of tuples, e.g. [(w1, l1), ... (wn, ln)] where
    w1 = width of rectangle 1,
    l1 = length of rectangle 1, etc.
--------------------------------------------------
RETURNS: a list of tuples that designate the top left corner placement,
         e.g. [(x1, y1), ... (xn, yn)] where
         x1 = top left x coordinate of rectangle 1 placement
         y1 = top left y coordinate of rectangle 1 placement, etc.
"""

def find_solution(rectangles):
    perimeter, positions = find_solution_by_y(rectangles, 50)
    return positions


def find_solution_varying(rectangles):
    num_runs = 100

    perimeter_list = []
    placements_list = []

    for i in range(num_runs):
        perimeter, placements = find_solution_by_x(rectangles, (i + 1) * 1)
        perimeter_list.insert(i, perimeter)
        placements_list.insert(i, placements)

    index = perimeter_list.index(min(perimeter_list))

    return placements_list[index]


def find_solution_by_x(rectangles, num_columns):
    column_width_increment = calc_column_increment_width(rectangles, num_columns)

    columns = [{} for i in range(num_columns)]
    placements = {}
    
    for index in range(len(rectangles)):

        width = rectangles[index][0]

        column_number = int(width / column_width_increment)

        if (column_number >= num_columns):
            column_number = num_columns - 1

        columns[column_number][index] = rectangles[index]
        
    upper_left_x = 0

    for col_index in range(num_columns):
        for key, value in place_in_columns_vertically(upper_left_x, columns[col_index]).items():
            placements[key] = value
        upper_left_x = upper_left_x + get_max_width(columns[col_index])

    perimeter = find_perimeter_by_x(columns, num_columns, column_width_increment)
    
    return perimeter, extract_placements(placements)


def find_solution_by_y(rectangles, num_rows):
    row_height_increment = calc_row_increment_height(rectangles, num_rows)

    rows = [{} for i in range(num_rows)]
    placements = {}

    for index in range(len(rectangles)):

        height = rectangles[index][1]

        row_number = int(height / row_height_increment)

        if (row_number >= num_rows):
            row_number = num_rows - 1

        rows[row_number][index] = rectangles[index]

    upper_left_y = 0

    for row_index in range(num_rows):
        for key, value in place_in_columns_horizontally(upper_left_y, rows[row_index]).items():
            placements[key] = value
        upper_left_y = upper_left_y - get_max_height(rows[row_index])

    perimeter = find_perimeter_by_y(rows, num_rows, row_height_increment)

    return perimeter, extract_placements(placements)


def get_max_width(some_boxes_dict):
    widths = []
    for key, value in some_boxes_dict.items():
        widths.append(value[0])
    return max(widths)


def get_max_height(some_boxes_dict):
    heights = []
    for key, value in some_boxes_dict.items():
        heights.append(value[1])
    return max(heights)


def max_width_of_list(some_boxes):
    widths = []
    for i in range(len(some_boxes)):
        widths.append(some_boxes[i][0])
    return max(widths)


def max_height_of_list(some_boxes):
    heights = []
    for i in range(len(some_boxes)):
        heights.append(some_boxes[i][1])
    return max(heights)


def min_width_of_list(some_boxes):
    widths = []
    for i in range(len(some_boxes)):
        widths.append(some_boxes[i][0])
    return min(widths)


def min_height_of_list(some_boxes):
    heights = []
    for i in range(len(some_boxes)):
        heights.append(some_boxes[i][1])
    return min(heights)


def calc_column_increment_width(rectangles, num_columns):
    min_width = min_width_of_list(rectangles)
    max_width = max_width_of_list(rectangles)
    d_width = max_width - min_width
    return ((d_width + 1) / (num_columns))


def calc_row_increment_height(rectangles, num_columns):
    min_height = min_height_of_list(rectangles)
    max_height = max_height_of_list(rectangles)
    d_height = max_height - min_height
    return ((d_height + 1) / (num_columns))


def place_in_columns_vertically(upper_left_x, some_boxes):
    placement = {}
    upper_left_y = 0
    
    for key, value in some_boxes.items():
        height = value[1]
        upper_left_y = upper_left_y + height
        coordinate = (upper_left_x, upper_left_y)
        placement[key] = coordinate
    
    return placement


def place_in_columns_horizontally(upper_left_y, some_boxes):
    placement = {}
    upper_left_x = 0

    for key, value in some_boxes.items():
        width = value[0]
        upper_left_x = upper_left_x - width
        coordinate = (upper_left_x, upper_left_y)
        placement[key] = coordinate

    return placement


def extract_placements(placement_dict):
    final_placement = []
    for key, value in placement_dict.items():
        final_placement.insert(key, value)
    return final_placement


def find_perimeter_by_x(columns, num_columns, column_width_increment):
    x = num_columns * column_width_increment
    max_column_height = 0
    for i in range(len(columns)):
        cur_height = get_column_height(columns[i]) 
        if (cur_height > max_column_height):
            max_column_height = cur_height
    y = max_column_height
    return (2 * y) + (2 * x)


def find_perimeter_by_y(rows, num_rows, column_height_increment):
    y = num_rows * column_height_increment
    max_row_length = 0
    for i in range(len(rows)):
        cur_length = get_row_length(rows[i])
        if (cur_length > max_row_length):
            max_row_length = cur_length
    x = max_row_length
    return (2 * y) + (2 * x)


def get_column_height(column_dict):
    column_height = 0
    for key, value, in column_dict.items():
        column_height = column_height + value[1]
    return column_height


def get_row_length(row_dict):
    row_length = 0
    for key, value in row_dict.items():
        row_length = row_length + value[0]
    return row_length







