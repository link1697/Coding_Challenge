import unittest
from main import Operation, Error
 
class TestListModify(unittest.TestCase):
    def test_list_modify_success(self):
        # Test when the length of the list is a multiple of 10
        test_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  
        result = Operation.list_modify(test_list)
        self.assertEqual(result, [1, 5, 7])

    def test_list_modify_failure(self):
        # Test when the length of the list is not a multiple of 10
        test_list = [0, 1, 2, 3, 4]  
        with self.assertRaises(Error) as catch_error:
            Operation.list_modify(test_list)
        self.assertEqual(catch_error.exception.id, 0)

if __name__ == '__main__':
    unittest.main()