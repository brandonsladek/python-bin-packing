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

if __name__ == '__main__':
    unittest.main()


