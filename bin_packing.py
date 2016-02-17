
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
    return find_solution_by_x(rectangles, 100)


def find_solution_by_x(rectangles, num_columns):

    column_width_increment = calc_column_increment(rectangles, num_columns)

    columns = [{} for i in range(num_columns)]
    placements = {}
    
    for index in range(len(rectangles)):

        width = rectangles[index][0]

        column_number = int (width / column_width_increment)

        if(column_number >= num_columns):
            column_number = num_columns - 1

        columns[column_number][index] = rectangles[index]
        
    upper_left_x = 0

    for col_index in range(num_columns):
        for key, value in place_in_columns(upper_left_x, columns[col_index]).items():
            placements[key] = value
        upper_left_x = upper_left_x + get_max_width(columns[col_index])
    
    return extract_placements(placements)


def get_max_width(some_boxes):
    widths = []
    for key, value in some_boxes.items():
        widths.append(value[0])
    return max(widths)


def max_width_of_list (some_boxes):
    widths = []
    for i in range(len(some_boxes)):
        widths.append(some_boxes[i][0])
    return max(widths);


def min_width_of_list (some_boxes):
    widths = []
    for i in range(len(some_boxes)):
        widths.append(some_boxes[i][0])
    return min(widths);


def calc_column_increment(rectangles, num_columns):
    min_width = min_width_of_list(rectangles)
    max_width = max_width_of_list(rectangles)
    d_width = max_width - min_width;
    return int (d_width / (num_columns))


def place_in_columns(upper_left_x, some_boxes):
    placement = {}
    upper_left_y = 0
    
    for key, value in some_boxes.items():
        height = value[1]
        upper_left_y = upper_left_y - height
        coordinate = (upper_left_x, upper_left_y)
        placement[key] = coordinate
    
    return placement


def extract_placements(placement_dict):
    final_placement = []
    for key, value in placement_dict.items():
        final_placement.insert(key, value)
    return final_placement


def extract(placement_list):
    final_placement = []
    for dictionary in placement_list:
        for key, value in dictionary.items():
            final_placement.insert(key, value)

    return final_placement