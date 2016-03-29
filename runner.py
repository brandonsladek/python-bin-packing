import paxtonDriver
# import bin_packing
# import time


# def run25times():

# 	total_perc = 0

# 	for i in range(25):
# 		paxtonDriver.generate_file("squares.txt", 1, 1000, 2500)

# 		rectangles = paxtonDriver.read_file("squares.txt")
# 		clone = rectangles[:]
# 		start = time.time()
# 		upper_left_coordinates = bin_packing.find_solution(clone)
# 		time_elapsed = time.time() - start

# 		print("Time elapsed in seconds =", time_elapsed)

# 		rectangle_coordinates = paxtonDriver.corner_coordinates(rectangles, upper_left_coordinates)
# 		naive_left_coordinates = paxtonDriver.find_naive_solution(rectangles)
# 		naive_rectangle_coordinates = paxtonDriver.corner_coordinates(rectangles, naive_left_coordinates)
# 		naive_perimeter = paxtonDriver.evaluate_solution(naive_rectangle_coordinates)
# 		print("Bounding Rectangle Perimeter of Naive Solution =", naive_perimeter)

# 		if paxtonDriver.is_solution_valid(rectangle_coordinates):
# 			perimeter = paxtonDriver.evaluate_solution(rectangle_coordinates)
# 			print("Bounding Rectangle Perimeter of Your Solution =", perimeter)
# 			if time_elapsed > 5.0:
# 				print("Error. Time Limit Exceeded.")
# 				perimeter = 2 * naive_perimeter

# 		percentage_improvement = (100 - (perimeter / naive_perimeter) * 100)
# 		print("Percentage Improvement Over Naive Solution =", percentage_improvement)

# 		total_perc = total_perc + percentage_improvement

# 	avg_perc = total_perc / 25

# 	print("AVERAGE PERCENTAGE IMPROVEMENT: ", avg_perc)


#run25times()

def run100times():
	for i in range(100):
		paxtonDriver.generate_file("squares.txt", 1, 1000, 2500)
		paxtonDriver.solve_problem("squares.txt")


run100times()
