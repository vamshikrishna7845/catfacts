import unittest 



class TestGetFacts(unittest.TestCase):
    @classmethod 
    def setUpClass(cls) -> None:
        return super().setUpClass()

    @classmethod
    def tearDownClass(cls) -> None:
        return super().tearDownClass()

    def setUp(self) -> None:
        return super().setUp()

    def tearDown(self) -> None:
        return super().tearDown()

    def test01_name(self):
        pass 

if __name__ == '__main__':
    unittest.main(verbosity=True)