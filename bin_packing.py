
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
    return find_solution_by_x(rectangles)



def find_solution_by_x(rectangles):
    num_columns = 10;
    column_width_increment = calc_column_increment(rectangles, num_columns)
    print("Increment: " + str (column_width_increment))

    columns = [{} for i in range(num_columns)]
    
    for index in range(len(rectangles)):

        width = rectangles[index][0]

        column_number = int (width / column_width_increment)
        if(column_number >= num_columns):
            column_number = num_columns - 1

        # print("Width: " + str (width))
        # print("Column Number: " + str (column_number))

        # print (str(index))
        columns[column_number][index] = rectangles[index]
        # dictionary = columns[column_number]
        # dictionary[index] = rectangles[index]


    upper_left_x = 0
    for col_index in range(num_columns):
        for key, value in place_in_columns(upper_left_x, columns[col_index]).items():
            columns[col_index][key] = value
        upper_left_x = upper_left_x + get_max_width(columns[col_index])
    
    return extract(columns)


def find_solution_by_100(rectangles):
    
    upper_left_x = 0
    
    column_placement = {}
    column_placement_0 = {}
    column_placement_1 = {}
    column_placement_2 = {}
    column_placement_3 = {}
    column_placement_4 = {}
    column_placement_5 = {}
    column_placement_6 = {}
    column_placement_7 = {}
    column_placement_8 = {}
    column_placement_9 = {}
    
    for index in range(len(rectangles)):
        
        width = rectangles[index][0]
        
        if width < 101:
            column_placement_0[index] = rectangles[index]
        elif width < 201:
            column_placement_1[index] = rectangles[index]
        elif width < 301:
            column_placement_2[index] = rectangles[index]
        elif width < 401:
            column_placement_3[index] = rectangles[index]
        elif width < 501:
            column_placement_4[index] = rectangles[index]
        elif width < 601:
            column_placement_5[index] = rectangles[index]
        elif width < 701:
            column_placement_6[index] = rectangles[index]
        elif width < 801:
            column_placement_7[index] = rectangles[index]
        elif width < 901:
            column_placement_8[index] = rectangles[index]
        elif width < 1001:
            column_placement_9[index] = rectangles[index]
    
    for key, value in place_in_columns(0, column_placement_0).items():
        column_placement[key] = value
    upper_left_x = upper_left_x + get_max_width(column_placement_0)

    for key, value in place_in_columns(upper_left_x, column_placement_1).items():
        column_placement[key] = value
    upper_left_x = upper_left_x + get_max_width(column_placement_1)
    
    for key, value in place_in_columns(upper_left_x, column_placement_2).items():
        column_placement[key] = value
    upper_left_x = upper_left_x + get_max_width(column_placement_2)

    for key, value in place_in_columns(upper_left_x, column_placement_3).items():
        column_placement[key] = value
    upper_left_x = upper_left_x + get_max_width(column_placement_3)
    
    for key, value in place_in_columns(upper_left_x, column_placement_4).items():
        column_placement[key] = value
    upper_left_x = upper_left_x + get_max_width(column_placement_4)

    for key, value in place_in_columns(upper_left_x, column_placement_5).items():
        column_placement[key] = value
    upper_left_x = upper_left_x + get_max_width(column_placement_5)
    
    for key, value in place_in_columns(upper_left_x, column_placement_6).items():
        column_placement[key] = value
    upper_left_x = upper_left_x + get_max_width(column_placement_6)

    for key, value in place_in_columns(upper_left_x, column_placement_7).items():
        column_placement[key] = value
    upper_left_x = upper_left_x + get_max_width(column_placement_7)
    
    for key, value in place_in_columns(upper_left_x, column_placement_8).items():
        column_placement[key] = value
    upper_left_x = upper_left_x + get_max_width(column_placement_8)

    for key, value in place_in_columns(upper_left_x, column_placement_9).items():
        column_placement[key] = value
    
    return extract_placements(column_placement)


def find_solution_by_50(rectangles):
    
    upper_left_x = 0
    
    column_placement = {}
    column_placement_0 = {}
    column_placement_1 = {}
    column_placement_2 = {}
    column_placement_3 = {}
    column_placement_4 = {}
    column_placement_5 = {}
    column_placement_6 = {}
    column_placement_7 = {}
    column_placement_8 = {}
    column_placement_9 = {}
    column_placement_10 = {}
    column_placement_11 = {}
    column_placement_12 = {}
    column_placement_13 = {}
    column_placement_14 = {}
    column_placement_15 = {}
    column_placement_16 = {}
    column_placement_17 = {}
    column_placement_18 = {}
    column_placement_19 = {}
    
    for index in range(len(rectangles)):
        
        width = rectangles[index][0]
        
        if width < 51:
            column_placement_0[index] = rectangles[index]
        elif width < 101:
            column_placement_1[index] = rectangles[index]
        elif width < 151:
            column_placement_2[index] = rectangles[index]
        elif width < 201:
            column_placement_3[index] = rectangles[index]
        elif width < 251:
            column_placement_4[index] = rectangles[index]
        elif width < 301:
            column_placement_5[index] = rectangles[index]
        elif width < 351:
            column_placement_6[index] = rectangles[index]
        elif width < 401:
            column_placement_7[index] = rectangles[index]
        elif width < 451:
            column_placement_8[index] = rectangles[index]
        elif width < 501:
            column_placement_9[index] = rectangles[index]
        elif width < 551:
            column_placement_10[index] = rectangles[index]
        elif width < 601:
            column_placement_11[index] = rectangles[index]
        elif width < 651:
            column_placement_12[index] = rectangles[index]
        elif width < 701:
            column_placement_13[index] = rectangles[index]
        elif width < 751:
            column_placement_14[index] = rectangles[index]
        elif width < 801:
            column_placement_15[index] = rectangles[index]
        elif width < 851:
            column_placement_16[index] = rectangles[index]
        elif width < 901:
            column_placement_17[index] = rectangles[index]
        elif width < 951:
            column_placement_18[index] = rectangles[index]
        elif width < 1001:
            column_placement_19[index] = rectangles[index]
    
    for key, value in place_in_columns(0, column_placement_0).items():
        column_placement[key] = value
    upper_left_x = upper_left_x + get_max_width(column_placement_0)

    for key, value in place_in_columns(upper_left_x, column_placement_1).items():
        column_placement[key] = value
    upper_left_x = upper_left_x + get_max_width(column_placement_1)
    
    for key, value in place_in_columns(upper_left_x, column_placement_2).items():
        column_placement[key] = value
    upper_left_x = upper_left_x + get_max_width(column_placement_2)
    
    for key, value in place_in_columns(upper_left_x, column_placement_3).items():
        column_placement[key] = value
    upper_left_x = upper_left_x + get_max_width(column_placement_3)
    
    for key, value in place_in_columns(upper_left_x, column_placement_4).items():
        column_placement[key] = value
    upper_left_x = upper_left_x + get_max_width(column_placement_4)
    
    for key, value in place_in_columns(upper_left_x, column_placement_5).items():
        column_placement[key] = value
    upper_left_x = upper_left_x + get_max_width(column_placement_5)
    
    for key, value in place_in_columns(upper_left_x, column_placement_6).items():
        column_placement[key] = value
    upper_left_x = upper_left_x + get_max_width(column_placement_6)
    
    for key, value in place_in_columns(upper_left_x, column_placement_7).items():
        column_placement[key] = value
    upper_left_x = upper_left_x + get_max_width(column_placement_7)
    
    for key, value in place_in_columns(upper_left_x, column_placement_8).items():
        column_placement[key] = value
    upper_left_x = upper_left_x + get_max_width(column_placement_8)
    
    for key, value in place_in_columns(upper_left_x, column_placement_9).items():
        column_placement[key] = value
    upper_left_x = upper_left_x + get_max_width(column_placement_9)

    for key, value in place_in_columns(upper_left_x, column_placement_10).items():
        column_placement[key] = value
    upper_left_x = upper_left_x + get_max_width(column_placement_10)

    for key, value in place_in_columns(upper_left_x, column_placement_11).items():
        column_placement[key] = value
    upper_left_x = upper_left_x + get_max_width(column_placement_11)

    for key, value in place_in_columns(upper_left_x, column_placement_12).items():
        column_placement[key] = value
    upper_left_x = upper_left_x + get_max_width(column_placement_12)

    for key, value in place_in_columns(upper_left_x, column_placement_13).items():
        column_placement[key] = value
    upper_left_x = upper_left_x + get_max_width(column_placement_13)

    for key, value in place_in_columns(upper_left_x, column_placement_14).items():
        column_placement[key] = value
    upper_left_x = upper_left_x + get_max_width(column_placement_14)

    for key, value in place_in_columns(upper_left_x, column_placement_15).items():
        column_placement[key] = value
    upper_left_x = upper_left_x + get_max_width(column_placement_15)

    for key, value in place_in_columns(upper_left_x, column_placement_16).items():
        column_placement[key] = value
    upper_left_x = upper_left_x + get_max_width(column_placement_16)

    for key, value in place_in_columns(upper_left_x, column_placement_17).items():
        column_placement[key] = value
    upper_left_x = upper_left_x + get_max_width(column_placement_17)

    for key, value in place_in_columns(upper_left_x, column_placement_18).items():
        column_placement[key] = value
    upper_left_x = upper_left_x + get_max_width(column_placement_18)

    for key, value in place_in_columns(upper_left_x, column_placement_19).items():
        column_placement[key] = value

    return extract_placements(column_placement)


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