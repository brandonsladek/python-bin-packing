import unittest
import bin_packing

class TestBinPackingMethods(unittest.TestCase):

    def setUp(self):
        self.boxes_dict = {}
        self.boxes_dict[1] = (4, 5)
        self.boxes_dict[2] = (7, 9)
        self.boxes_dict[3] = (5, 8)
    
        self.placement = {}
        self.placement[1] = (0, 0)
        self.placement[2] = (0, -5)
        self.placement[3] = (0, -14)
    
        self.original_list = [(1,3), (4,5), (8,9)]
    
    def test_get_max_width(self):
        max_width = bin_packing.get_max_width(self.boxes_dict)
        self.assertEqual(7, max_width)

    def test_place_in_columns(self):
        placement_dictionary = {}
        placement_dictionary = bin_packing.place_in_columns(0, self.boxes_dict)

        self.assertEqual(placement_dictionary[1], (0, 0))
        self.assertEqual(placement_dictionary[2], (0, -5))
        self.assertEqual(placement_dictionary[3], (0, -14))

        placement_dictionary = bin_packing.place_in_columns(201, self.boxes_dict)

        self.assertEqual(placement_dictionary[1], (201, 0))
        self.assertEqual(placement_dictionary[2], (201, -5))
        self.assertEqual(placement_dictionary[3], (201, -14))

    def test_extract_placements(self):
        final_placement = {}
        final_placement = bin_packing.extract_placements(self.placement)

        self.assertEqual(final_placement, [(0, 0), (0, -5), (0, -14)])

    def test_height_extract(self):
        height_1 = self.original_list[0][1]
        height_2 = self.original_list[1][1]
        height_3 = self.original_list[2][1]

        self.assertEqual(height_1, 3)
        self.assertEqual(height_2, 5)
        self.assertEqual(height_3, 9)

    def test_col_decision(self):
        column1 = {}
        column2 = {}
        column3 = {}

        for i in range(len(self.original_list)):

            width = self.original_list[i][0]

            if width < 2:
                column1[i] = self.original_list[i]
            elif width < 5:
                column2[i] = self.original_list[i]
            elif width < 9:
                column3[i] = self.original_list[i]

        self.assertEqual(column1[0], (1,3))
        self.assertEqual(column2[1], (4,5))
        self.assertEqual(column3[2], (8,9))


if __name__ == '__main__':
    unittest.main()


