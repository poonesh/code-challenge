import unittest
import csv
from challenge2 import sort_csv, sorting_func

def compare_function(row1, row2):
	result1 = sorting_func(row1)
	result2 = sorting_func(row2)
	if result1[0] > result2[0]:
		return False
	if result1[0] < result2[0]:
		return True
	#compare year
	if result1[1] < result2[1]:
		return True
	if result1[1] > result2[1]:
		return False
	# compare month if year is equal
	if result1[2] > result2[2]:
		return False
	if result1[2] < result2[2]:
		return True
	# compare day if month is equal
	if result1[3] > result2[3]:
		return False
	if result1[3] <= result2[3]:
		return True



class Challenge2_Test(unittest.TestCase):

	def test_sorting_function(self):
		data_row1 = ["1","33","98","25","50","2001-05-18"]
		result1 = (1, 2001, 5, 18)
		data_row2 = ["1","5","26","14","72","1/17/18"]
		result2 = (1, 2018, 1, 17)
		
		self.assertEqual(sorting_func(data_row1), result1)
		self.assertEqual(sorting_func(data_row2), result2)

	def test_sorting_large_data(self):
		sort_csv('large_data.csv', 'large_data_sorted.csv')
		with open('large_data_sorted.csv', 'r') as csv_file:
			csv_reader = csv.reader(csv_file, delimiter=',')
			next(csv_reader)
			previous_line = next(csv_reader)
			for line in csv_reader:
				current_line = line
				result = compare_function(previous_line, current_line)
				self.assertEqual(result, True)
				previous_line = current_line



if __name__ == '__main__':
    unittest.main()