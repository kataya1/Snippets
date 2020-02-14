'''
1.creeate a new file and name it test_{name of file to be tested}.py 
2.import unittest (standard python module)
3.import {name of file to bet tested}
4. make a test class that inherits from (unittest.TestCasee)
5. maake a function that compares a value you expect to come out with actual using assert() functions
6. navigate to command line and test it using "python -m unittest test_{file name}.py" command 
7. but instead of that you can write the unittest.main line of code and run this file directly
'''
import unittest
import file1


class TestFile1(unittest.TestCase):
    # how it runs: setUp -> test_div -> tearDown -> setUp -> test_sum -> tearDown
    def setUp(self):
        # this function runs befor every test method 
        pass
    def tearDown(self):
        # this function runs after every test method
        pass

    # tests doesn't necesseraily run in order
    def test_sum(self):  
    # if you write it as sum_test it wont register 
        self.assertEqual(file1.add(10,2,3),15)
        self.assertEqual(file1.add(-1,1),0)
        self.assertEqual(file1.add(-1,-1),-2)
    def test_div(self):  
        self.assertEqual(file1.div(10,2),5)
        self.assertEqual(file1.div(-1,-1),1)
        self.assertRaises(ValueError ,file1.div, 1, 0)
        with self.assertRaises(ZeroDivisionError):
            file1.div(1,0)
    
    # how it runs: setUpClass -> setUp -> test_div -> tearDown -> setUp -> test_sum -> tearDown -> tearDownClass
    @classmethod
    def setUpClass(cls):
        # these run before the class 
        pass
    @classmethod
    def tearDownClass(cls):
        # these run after the class 
        pass

if __name__ == "__main__": 
    # this way you can run the file directly (vscode has built in testing functionality)
    unittest.main()

'''you can use VS-Code ctrl+shift+p > python: Discover test'''