import unittest

class TestClass(unittest.TestCase):
    def setUp(self):
        self.test_dir = "Set up"
        print(self.test_dir)

    def tearDown(self):
        # Remove the directory after the test
        print("Closing all test cases")

    def test_createLeaf(self):
        self.tup1= ('Fish','12345','https://groceries.morrisons.com/browse/178974/178969')
        print("Executing the test method")

if __name__ == '__main__':
    unittest.main()
        