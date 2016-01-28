
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
    
    upper_left_x = 0
    
    column_placement = []
    column_placement_0 = []
    column_placement_1 = []
    column_placement_2 = []
    column_placement_3 = []
    column_placement_4 = []
    column_placement_5 = []
    column_placement_6 = []
    column_placement_7 = []
    column_placement_8 = []
    column_placement_9 = []
    
    final_placement = []
    
    for index in range(len(rectangles)-1):
        
        width = rectangles[index][0]
        
        if width < 101:
            column_placement_0.append((index, rectangles[index]))
        elif width < 201:
            column_placement_1.append((index, rectangles[index]))
        elif width < 301:
            column_placement_2.append((index, rectangles[index]))
        elif width < 401:
            column_placement_3.append((index, rectangles[index]))
        elif width < 501:
            column_placement_4.append((index, rectangles[index]))
        elif width < 601:
            column_placement_5.append((index, rectangles[index]))
        elif width < 701:
            column_placement_6.append((index, rectangles[index]))
        elif width < 801:
            column_placement_7.append((index, rectangles[index]))
        elif width < 901:
            column_placement_8.append((index, rectangles[index]))
        elif width < 1001:
            column_placement_9.append((index, rectangles[index]))

    column_placement.append(place_in_columns(0, column_placement_0))
    upper_left_x = upper_left_x + get_max_width(column_placement_0)+1
    print('column placement 0' + str(column_placement_0))
    print('max width col 0: ' + str(get_max_width(column_placement_0)))
    
    column_placement.append(place_in_columns(upper_left_x, column_placement_1))
    upper_left_x = upper_left_x + get_max_width(column_placement_1)+1

    column_placement.append(place_in_columns(upper_left_x, column_placement_2))
    upper_left_x = upper_left_x + get_max_width(column_placement_2)+1

    column_placement.append(place_in_columns(upper_left_x, column_placement_3))
    upper_left_x = upper_left_x + get_max_width(column_placement_3)+1

    column_placement.append(place_in_columns(upper_left_x, column_placement_4))
    upper_left_x = upper_left_x + get_max_width(column_placement_4)+1

    column_placement.append(place_in_columns(upper_left_x, column_placement_5))
    upper_left_x = upper_left_x + get_max_width(column_placement_5)+1

    column_placement.append(place_in_columns(upper_left_x, column_placement_6))
    upper_left_x = upper_left_x + get_max_width(column_placement_6)+1

    column_placement.append(place_in_columns(upper_left_x, column_placement_7))
    upper_left_x = upper_left_x + get_max_width(column_placement_7)+1

    column_placement.append(place_in_columns(upper_left_x, column_placement_8))
    upper_left_x = upper_left_x + get_max_width(column_placement_8)+1
    
    column_placement.append(place_in_columns(upper_left_x, column_placement_9))
    upper_left_x = upper_left_x + get_max_width(column_placement_9)+1
    
    print(str(extract_placements(column_placement)))
    return extract_placements(column_placement)

def get_max_width(some_boxes):
    widths = []
    for index in range(len(some_boxes)):
        widths.append(some_boxes[index][1][0])
    return max(widths)

def get_final_placement(unsorted_placements):
    final_placement = []
    for tuple in unsorted_placements:
        final_placement.insert(unsorted_placements[0],unsorted_placements[1])
    return final_placement

def place_in_columns(upper_left_x, some_boxes):
    placement = []
    upper_left_y = 0
    
    for tuple in some_boxes:
        height = tuple[1][1]
        coordinate = (upper_left_x, upper_left_y)   # make a tuple
        placement.append((tuple[0], coordinate))
        upper_left_y = upper_left_y - height
    
    return placement

def extract_placements(tuples):
    
    final_placement = []
    for index in range(len(tuples)):
        final_placement.insert(tuples[index][0][0], tuples[index][1])
    return final_placement






# ----------------------------------------------
# CSCI 338, Spring 2016, Bin Packing Assignment
# Author: John Paxton
# Last Modified: January 18, 2016
# ----------------------------------------------

import random
import time


# -----------------------------------------------

"""
    GENERATE_FILE:
    Randomly produce rectangles and write them to a file
    --------------------------------------------------
    file_name: the name of the output file
    min_dimension: the smallest value for the width or length of a rectangle
    max_dimension: the largest value for the width or length of a rectangle
    number_rectangles: number of rectangles to generate
    --------------------------------------------------
    RETURNS: nothing
    
    """

def generate_file(file_name, min_dimension, max_dimension, number_rectangles):
    file = open(file_name, "w")
    
    min_dimension = int(min_dimension)  # must be an integer
    if min_dimension < 1:               # minimum value is 1
        min_dimension = 1
    
    max_dimension = int(max_dimension)  # must be an integer
    if max_dimension > 1000:            # maximum value is 1000
        max_dimension = 1000
    
    if min_dimension > max_dimension:   # swap if necessary
        temp = min_dimension
        min_dimension = max_dimension
        max_dimension = temp
    
    for square in range(number_rectangles):
        width = random.randint(min_dimension, max_dimension)
        length = random.randint(min_dimension, max_dimension)
        file.write(str(width) + " " + str(length) + "\n")
    
    file.close()

generate_file("squares.txt", 1, 1000, 2500)

# -----------------------------------------------

"""
    FIND_NAIVE_SOLUTION:
    Line the the top left corners of the rectangles up along
    the y = 0 axis starting with (0,0).
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

def find_naive_solution (rectangles):
    placement = []
    upper_left_x = 0
    upper_left_y = 0
    
    for rectangle in rectangles:
        width = rectangle[0]
        coordinate = (upper_left_x, upper_left_y)   # make a tuple
        placement.insert(0, coordinate)             # insert tuple at front of list
        upper_left_x = upper_left_x + width
    
    placement.reverse()                             # original order
    return placement

# -----------------------------------------------

"""
    EVALUATE_SOLUTION:
    Find the perimeter of the rectangle that contains the packing.
    --------------------------------------------------
    coordinates: a list of tuples, e.g. [(a1, b1, c1, d1), ... (an, bn, cn, dn)] where
    a1 = upper left x of rectangle 1
    b1 = upper left y of rectangle 1
    c1 = lower right x of rectangle 1
    d1 = lower right y of rectangle 1, etc.
    --------------------------------------------------
    RETURNS: the perimeter of the bounding rectangle, an integer
    """

def evaluate_solution (coordinates):
    tuple = coordinates[1]              # grab first tuple of solution
    min_x = tuple[0]                    # initializing smallest x
    max_y = tuple[1]                    # initializing largest y
    max_x = tuple[2]                    # initializing largest x
    min_y = tuple[3]                    # initializing smallest y
    
    for coordinate in coordinates:
        
        top_left_x = coordinate[0]
        top_left_y = coordinate[1]
        lower_right_x = coordinate[2]
        lower_right_y = coordinate[3]
        
        if top_left_x < min_x:          # find smallest x value
            min_x = top_left_x
        if lower_right_x > max_x:       # find largest x value
            max_x = lower_right_x
        if top_left_y > max_y:          # find largest y value
            max_y = top_left_y
        if lower_right_y < min_y:       # find smallest y value
            min_y = lower_right_y

    bounding_rectangle_perimeter = 2 * ((max_x - min_x) + (max_y - min_y))
    return bounding_rectangle_perimeter

# -----------------------------------------------

"""
    CORNER_COORDINATES:
    Convert the solution to the upper left and lower right points.
    --------------------------------------------------
    dimensions: a list of tuples, e.g. [(w1, l1), ... (wn, ln)] where
    w1 = width of rectangle 1,
    l1 = length of rectangle 1, etc.
    upper_left: a list of tuples that designate the top left corner placement,
    e.g. [(x1, y1), ... (xn, yn)] where
    x1 = top left x coordinate of rectangle 1 placement
    y1 = top left y coordinate of rectangle 1 placement, etc.
    --------------------------------------------------
    RETURNS: a list of tuples, e.g. [(a1, b1, c1, d1), ... (an, bn, cn, dn)] where
    a1 = upper left x of rectangle 1
    b1 = upper left y of rectangle 1
    c1 = lower right x of rectangle 1
    d1 = lower right y of rectangle 1, etc.
    """

def corner_coordinates (dimensions, upper_left):
    answer = []
    
    for i in range(len(dimensions)):
        coordinate = upper_left[i]      # (x, y) of upper left
        dimension = dimensions[i]       # (width, length) of rectangle
        upper_x = coordinate[0]
        upper_y = coordinate[1]
        lower_x = upper_x + dimension[0]
        lower_y = upper_y - dimension[1]
        answer.insert(0, (upper_x, upper_y, lower_x, lower_y))
    
    answer.reverse()                    # original order
    return answer

# -----------------------------------------------

"""
    OVERLAP:
    Determine if two rectangles overlap
    --------------------------------------------------
    rectangle_1: a tuple e.g. (a1, b1, c1, d1)
    a1 = upper left x of rectangle 1
    b1 = upper left y of rectangle 1
    c1 = lower right x of rectangle 1
    d1 = lower right y of rectangle 1
    rectangle_2: similar to rectangle_1
    --------------------------------------------------
    RETURNS: True if the rectangles overlap, False if they don't
    """

def overlap(rectangle_1, rectangle_2):
    
    # if one rectangle is to the left of the other, there is no overlap
    if rectangle_1[2] <= rectangle_2[0] or rectangle_2[2] <= rectangle_1[0]:
        return False
    
    # if one rectangle is above the other, there is no overlap
    elif rectangle_1[3] >= rectangle_2[1] or rectangle_2[3] >= rectangle_1[1]:
        return False
    
    # otherwise there is overlap
    else:
        print("Error!  Overlapping rectangles: ", rectangle_1, rectangle_2)
        return True

# -----------------------------------------------

"""
    IS_SOLUTION_VALID:
    Determine if any pair of rectangles overlap.
    --------------------------------------------------
    coordinates: a list of tuple e.g. [(a1, b1, c1, d1), ... (an, bn, cn, dn)] where
    a1 = upper left x of rectangle 1
    b1 = upper left y of rectangle 1
    c1 = lower right x of rectangle 1
    d1 = lower right y of rectangle 1
    rectangle_2: similar to rectangle_1
    --------------------------------------------------
    RETURNS: True if any rectangles overlap, False if none do
    """

def is_solution_valid (coordinates):
    
    for i in range(len(coordinates)):
        rectangle_1 = coordinates[i]
        
        for j in range(i+1, len(coordinates)):
            rectangle_2 = coordinates[j]
            
            if overlap(rectangle_1, rectangle_2):
                return False

    return True

# -----------------------------------------------

"""
    READ_FILE:
    Read width and length of unspecified numbers of rectangles from a file
    --------------------------------------------------
    file_name: name of the input file
    --------------------------------------------------
    RETURNS: a list of tuples, e.g. [(w1, l1), ... (wn, ln)] where
    w1 = width of rectangle 1,
    l1 = length of rectangle 1, etc.
    """

def read_file(file_name):
    file = open(file_name, "r")
    next_line = file.readline()
    rectangles = []
    
    while next_line:
        dimensions = next_line.split()  # splits line into list of tokens
        width = int(dimensions[0])
        length = int(dimensions[1])
        rectangles.insert(0, (width, length))
        next_line = file.readline()
    
    rectangles.reverse()                # original order
    return rectangles

# -----------------------------------------------

"""
    SOLVE_PROBLEM:
    This is the main driver function.
    --------------------------------------------------
    file_name: name of the input file
    --------------------------------------------------
    RETURNS: nothing
    """

def solve_problem(file_name):
    rectangles = read_file(file_name)
    clone = rectangles[:]       # clone so that original info retained
    
    # get student solution and measure tie
    start = time.time()
    upper_left_coordinates = find_solution(clone)
    time_elapsed = time.time() - start
    print("Time elapsed in seconds =", time_elapsed)
    
    # convert student solution to show upper left and lower right coordinates
    rectangle_coordinates = corner_coordinates(rectangles, upper_left_coordinates)
    
    # get a solution using the naive method
    naive_left_coordinates = find_naive_solution(rectangles)
    naive_rectangle_coordinates = corner_coordinates(rectangles, naive_left_coordinates)
    naive_perimeter = evaluate_solution(naive_rectangle_coordinates)
    print("Bounding Rectangle Perimeter of Naive Solution =", naive_perimeter)
    
    
    if is_solution_valid (rectangle_coordinates):   # is student solution valid?
        perimeter = evaluate_solution(rectangle_coordinates)
        print("Bounding Rectangle Perimeter of Your Solution =", perimeter)
        if time_elapsed > 5.0:                      # is student solution fast enough?
            print("Error.  Time Limit Exceeded.")
            perimeter = 2 * naive_perimeter         # answer is penalized

    else:
        print("Error.  Overlapping Rectangles in Solution.")
        perimeter = 2 * naive_perimeter             # answer is penalized
    
    print("Percentage Improvement Over Naive Solution =", 100 - (perimeter / naive_perimeter) * 100)

# -----------------------------------------------

solve_problem("squares.txt")

