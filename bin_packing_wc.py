

import math



""" 
    Brandon Sladek & Alex Calderwood

    Strategy:
    
    We first find the box with the maximum width and the box with the minimum width and get the difference between the two. 
    Then, we divide that number by the number of columns that we wish to have in our solution. This gives us the "increment"
    value, how much wider each successive column is compared to the last. Then we have a list of dictionaries where each
    dictionary represents a group of boxes with similar widths. The boxes are placed into the list of dictionaries by
    dividing each boxes width by the "increment" value and taking the whole number of the division to be the index into the
    list. This way the boxes are separated into groups of boxes with similar widths. We then go through each dictionary in the
    list (each group of boxes) and place the boxes in columns, one column for each group of boxes with similar widths.

    We also do the same thing as above but with creating rows of boxes with similar heights, instead of columns of boxes
    with similar widths. This way if a set of boxes varies less in one dimension we can accommodate for that. Perhaps the most
    interesting part about our solution is that we can vary the number of columns or rows with each run of the algorithm. So our
    solution actually runs the algorithm 50 times in the column-placement manner, starting with 25 columns and ending with 74 
    columns. Then we run the algorithm 50 more times in the row-placement manner, again starting with 25 rows and ending with 74 
    rows. Finally, we calculate the perimeters for each of these solutions and only return the best one.

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
    return find_solution_by_varying(rectangles)

# This function runs the algorithm 50 times for each direction (columns vs rows) and returns the best solution
def find_solution_by_varying(rectangles):
    num_runs_each = 50

    # A list to hold the perimeter for each solution and a list to hold the placements for each solution
    perimeter_list = []
    placements_list = []

    for i in range(num_runs_each):
        # Run the algorithm in the column-stacking pattern 50 times, starting with 25 columns and ending 74
        perimeter_vertical, placements_vertical = find_solution_by_column_stacking(rectangles, 25 + i)
        perimeter_list.insert(i, perimeter_vertical)
        placements_list.insert(i, placements_vertical)

    for i in range(50, num_runs_each + 50):
        # Run the algorithm in the row-packing pattern 50 times, starting with 25 rows and ending with 74
        perimeter_horizontal, placements_horizontal = find_solution_by_row_packing(rectangles, i - 25)
        perimeter_list.insert(i, perimeter_horizontal)
        placements_list.insert(i, placements_horizontal)

    # Find the index of the solution with the smallest perimeter
    index = perimeter_list.index(min(perimeter_list))

    if index < 50:
        print("VERTICAL!")
    else:
        print("HORIZONTAL!")

    return placements_list[index]


# This function runs the algorithm in the column-stacking pattern creating a packing with the specified number of columns
def find_solution_by_column_stacking(rectangles, num_columns):
    # Calculate how much wider each successive column will be compared to the previous
    column_width_increment = calc_column_increment_width(rectangles, num_columns)

    # List of dictionaries to hold groups of boxes with similar widths
    columns = [{} for i in range(num_columns)]
    placements = {}
    
    for index in range(len(rectangles)):

        width = rectangles[index][0]

        # Determine the column the box should go in based on its width
        column_number = int(width / column_width_increment)

        # The widest boxes might have an invalid column number
        if (column_number >= num_columns):
            column_number = num_columns - 1

        # Put the box in the correct group and associate it with its original place in the dimensions list
        columns[column_number][index] = rectangles[index]
        
    height_to_use = get_height_to_use(columns, num_columns)[0]
    overflow_column = {}

    for z in range(num_columns):
        columns[z], overflow_column = chop_column_vertical(columns[z], overflow_column, height_to_use)

    #new_max_column_height = get_max_column_height(columns)

    overflow_cols = []
    overflow_cols = chop_overflow_column(overflow_column, height_to_use)

    for i in range(len(overflow_cols)):
        columns.insert(num_columns + i, overflow_cols[i])
    
    upper_left_x = 0

    # Go through each group and place the boxes into their columns
    for col_index in range(num_columns + len(overflow_cols)):
        for key, value in place_in_columns_vertically(upper_left_x, columns[col_index]).items():
            placements[key] = value
        # Calculate the new leftmost x-value of the next column
        upper_left_x = upper_left_x + get_max_width(columns[col_index])

    # Calculate perimeter of solution
    perimeter = find_perimeter_of_column_stacking(columns, num_columns, column_width_increment)
    
    return perimeter, extract_placements(placements)


# This function runs the algorithm in the row-packing pattern creating a packing with the specified number of rows
def find_solution_by_row_packing(rectangles, num_rows):
    # Calculate how much taller each successive row will be compared to the previous
    row_height_increment = calc_row_increment_height(rectangles, num_rows)

    # List of dictionaries to hold groups of boxes with similar heights
    rows = [{} for i in range(num_rows)]
    placements = {}

    for index in range(len(rectangles)):

        height = rectangles[index][1]

        # Determine the row the box should go in based on its height
        row_number = int(height / row_height_increment)

        # The tallest boxes might have an invalid row number
        if (row_number >= num_rows):
            row_number = num_rows - 1

        # Put the box in the correct group and associate it with its original place in the dimensions list
        rows[row_number][index] = rectangles[index]

    length_to_use = get_length_to_use(rows, num_rows)[0]
    overflow_row = {}

    for z in range(num_rows):
        rows[z], overflow_row = chop_row_horizontal(rows[z], overflow_row, length_to_use)

    overflow_rows = []
    overflow_rows = chop_overflow_row(overflow_row, length_to_use)

    for i in range(len(overflow_rows)):
        rows.insert(num_rows + i, overflow_rows[i])

    upper_left_y = 0

    # Go through each group and place the boxes into their rows
    for row_index in range(num_rows + len(overflow_rows)):
        for key, value in place_in_rows_horizontally(upper_left_y, rows[row_index]).items():
            placements[key] = value
        # Calculate the new uppermost y-value of the next row
        upper_left_y = upper_left_y - get_max_height(rows[row_index])

    # Calculate perimeter of solution
    perimeter = find_perimeter_of_row_packing(rows, num_rows, row_height_increment)

    return perimeter, extract_placements(placements)


def get_max_column_height(columns):
    max_column_height = 0
    for i in range(len(columns)):
        column_height = get_column_height(columns[i])
        if (column_height > max_column_height):
            max_column_height = column_height

    return max_column_height


# This function takes in a dictionary of boxes and returns the value of the largest width
def get_max_width(some_boxes_dict):
    widths = []
    for key, value in some_boxes_dict.items():
        widths.append(value[0])

    if (len(widths) == 0):
        return 0
    else:
        return max(widths)


# This function takes in a dictionary of boxes and returns the value of the largest height
def get_max_height(some_boxes_dict):
    heights = []
    for key, value in some_boxes_dict.items():
        heights.append(value[1])

    if (len(heights) == 0):
        return 0
    else:
        return max(heights)


# This function takes in a list of boxes and returns the value of the largest width
def max_width_of_list(some_boxes):
    widths = []
    for i in range(len(some_boxes)):
        widths.append(some_boxes[i][0])

    if (len(widths) == 0):
        return 0
    else:
        return max(widths)


# This function takes in a list of boxes and returns the value of the largest height
def max_height_of_list(some_boxes):
    heights = []
    for i in range(len(some_boxes)):
        heights.append(some_boxes[i][1])

    if (len(heights) == 0):
        return 0
    else:
        return max(heights)


# This function takes in a list of boxes and returns the value of the smallest width
def min_width_of_list(some_boxes):
    widths = []
    for i in range(len(some_boxes)):
        widths.append(some_boxes[i][0])

    if (len(widths) == 0):
        return 0
    else:
        return min(widths)


# This function takes in a list of boxes and returns the value of the smallest height
def min_height_of_list(some_boxes):
    heights = []
    for i in range(len(some_boxes)):
        heights.append(some_boxes[i][1])

    if (len(heights) == 0):
        return 0
    else:
        return min(heights)


# This function calculates how much wider each successive column should be
def calc_column_increment_width(rectangles, num_columns):
    min_width = min_width_of_list(rectangles)
    max_width = max_width_of_list(rectangles)
    d_width = max_width - min_width

    return ((d_width + 1) / (num_columns))


# This function calculates how much taller each successive row should be
def calc_row_increment_height(rectangles, num_rows):
    min_height = min_height_of_list(rectangles)
    max_height = max_height_of_list(rectangles)
    d_height = max_height - min_height

    return ((d_height + 1) / (num_rows))


# This function places boxes in a column according to the upper left x-value passed in
def place_in_columns_vertically(upper_left_x, some_boxes):
    placement = {}
    upper_left_y = 0
    
    # Go through each box and increment their y-value placements accordingly
    for key, value in some_boxes.items():
        height = value[1]
        upper_left_y = upper_left_y + height
        coordinate = (upper_left_x, upper_left_y)
        # Keep track of where the box was in the original dimensions list
        placement[key] = coordinate
    
    return placement


# This function places boxes in a row according to the upper left y-value passed in
def place_in_rows_horizontally(upper_left_y, some_boxes):
    placement = {}
    upper_left_x = 0

    # Go through each box and increment their x-value placements accordingly
    for key, value in some_boxes.items():
        width = value[0]
        upper_left_x = upper_left_x - width
        coordinate = (upper_left_x, upper_left_y)
        # Keep track of where the box was in the original dimensions list
        placement[key] = coordinate

    return placement


# This function takes in a dictionary of placements and returns a list of placements in the correct order
def extract_placements(placement_dict):
    final_placement = []
    for key, value in placement_dict.items():
        # The key here is the index the box had in the original dimensions list
        final_placement.insert(key, value)

    return final_placement


# This function calculates the perimeter of a column-stacked solution
def find_perimeter_of_column_stacking(columns, num_columns, column_width_increment):
    # Calculate the total width of the packing
    x = calc_total_width(num_columns, column_width_increment)
    max_column_height = 0

    # Find the value of the height of the tallest column
    for i in range(len(columns)):
        cur_height = get_column_height(columns[i]) 
        if (cur_height > max_column_height):
            max_column_height = cur_height

    y = max_column_height

    # Calculate perimeter and return
    return (2 * y) + (2 * x)


# This function calculates the perimeter of a row-packed solution
def find_perimeter_of_row_packing(rows, num_rows, column_height_increment):
    # Calculate the total height of the packing
    y = calc_total_height(num_rows, column_height_increment)
    max_row_length = 0

    # Find the value of the length of the longest row
    for i in range(len(rows)):
        cur_length = get_row_length(rows[i])
        if (cur_length > max_row_length):
            max_row_length = cur_length

    x = max_row_length

    # Calculate perimeter and return
    return (2 * y) + (2 * x)


# This function takes in a dictionary of boxes in a column and returns the height of the column
def get_column_height(column_dict):
    column_height = 0
    for key, value, in column_dict.items():
        column_height = column_height + value[1]

    return column_height


# This function takes in a dictionary of boxes in a row and returns the length of the row
def get_row_length(row_dict):
    row_length = 0
    for key, value in row_dict.items():
        row_length = row_length + value[0]

    return row_length


# This function calculates the total width of the column-stacked packing
def calc_total_width(num_columns, column_width_increment):
    col_width = 0
    total_width = 0

    # Go through each column and add its width to the total width
    for i in range(num_columns):
        col_width = col_width + column_width_increment
        total_width = total_width + col_width

    return total_width


def get_height_to_use(columns, num_columns):
    total_columns_height = 0
    min_column_height = 10000000000

    for z in range(num_columns):
        column_height = get_column_height(columns[z])
        total_columns_height = total_columns_height + column_height

        if (column_height < min_column_height):
            min_column_height = column_height

    avg_column_height = total_columns_height / num_columns
    height_to_use = min_column_height + ((avg_column_height - min_column_height) / 2)

    return height_to_use, min_column_height


def get_length_to_use(rows, num_rows):
    total_rows_length = 0
    min_row_length = 10000000000

    for z in range(num_rows):
        row_length = get_row_length(rows[z])
        total_rows_length = total_rows_length + row_length

        if (row_length < min_row_length):
            min_row_length = row_length

    avg_row_length = total_rows_length / num_rows
    length_to_use = min_row_length + ((avg_row_length - min_row_length) / 2)

    return length_to_use, min_row_length


def chop_column_vertical(col_to_chop, overflow_col, height_to_use):
    current_height = 0
    keys_to_delete = []
    
    for key, value in col_to_chop.items():
        if current_height < height_to_use:
            current_height = current_height + value[1]
        else:
            overflow_col[key] = value
            keys_to_delete.append(key)

    for key in keys_to_delete:
        del col_to_chop[key]

    return col_to_chop, overflow_col


def chop_row_horizontal(col_to_chop, overflow_col, length_to_use):
    current_length = 0
    keys_to_delete = []

    for key, value in col_to_chop.items():
        if current_length < length_to_use:
            current_length = current_length + value[0]
        else:
            overflow_col[key] = value
            keys_to_delete.append(key)

    for key in keys_to_delete:
        del col_to_chop[key]

    return col_to_chop, overflow_col


def chop_overflow_column(overflow_to_chop, height_to_use):
    current_height = 0
    col_num = 0

    height_of_overflow = get_column_height(overflow_to_chop)
    num_of_overflows = math.ceil(height_of_overflow / height_to_use)

    sorted_by_width = sorted(overflow_to_chop.items(), key = lambda x: x[1][0], reverse=True)

    overflow_cols = [{} for i in range(num_of_overflows)]

    for i in range(len(sorted_by_width)):
        if current_height < height_to_use:
            current_height = current_height + sorted_by_width[i][1][1]
            overflow_cols[col_num][sorted_by_width[i][0]] = sorted_by_width[i][1]
        else:
            col_num = col_num + 1
            overflow_cols[col_num][sorted_by_width[i][0]] = sorted_by_width[i][1]
            current_height = sorted_by_width[i][1][1]

    # for key, value in overflow_to_chop.items():
    #     if current_height < height_to_use:
    #         current_height = current_height + value[1]
    #         overflow_cols[col_num][key] = value
    #     else:
    #         col_num = col_num + 1
    #         overflow_cols[col_num][key] = value
    #         current_height = value[1]

    return overflow_cols


def chop_overflow_row(overflow_to_chop, length_to_use):
    current_length = 0
    row_num = 0

    length_of_overflow = get_row_length(overflow_to_chop)
    num_of_overflows = math.ceil(length_of_overflow / length_to_use)

    sorted_by_height = sorted(overflow_to_chop.items(), key = lambda x: x[1][1], reverse=True)

    overflow_rows = [{} for i in range(num_of_overflows)]

    for i in range(len(sorted_by_height)):
        if current_length < length_to_use:
            current_length = current_length + sorted_by_height[i][1][0]
            overflow_rows[row_num][sorted_by_height[i][0]] = sorted_by_height[i][1]
        else:
            row_num = row_num + 1
            overflow_rows[row_num][sorted_by_height[i][0]] = sorted_by_height[i][1]
            current_length = sorted_by_height[i][1][0]

    # for key, value in overflow_to_chop.items():
    #     if current_length < length_to_use:
    #         current_length = current_length + value[0]
    #         overflow_rows[row_num][key] = value
    #     else:
    #         row_num = row_num + 1
    #         overflow_rows[row_num][key] = value
    #         current_length = value[0]

    return overflow_rows


# This function calculates the total height of the row-packed packing
def calc_total_height(num_rows, row_height_increment):
    row_height = 0
    total_height = 0

    # Go through each row and add its height to the total height
    for i in range(num_rows):
        row_height = row_height + row_height_increment
        total_height = total_height + row_height

    return total_height
