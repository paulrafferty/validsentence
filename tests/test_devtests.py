import unittest
from validsentence.Validator import Validator

class DevTest(unittest.TestCase):

    """This class tests the private functions in the Validator class"""

    def test_capital(self):
        """Form of test necessary to call and test private functions"""
        assert Validator()._Validator__check_capital('Pass') == True
        assert Validator()._Validator__check_capital('Pass') == True
        assert Validator()._Validator__check_capital('fail') == False
        assert Validator()._Validator__check_capital('1234') == False
        assert Validator()._Validator__check_capital('.Capital') == False

    def test_quotes(self):
        assert Validator()._Validator__check_quotes('This "should" pass') == True
        assert Validator()._Validator__check_quotes('This "should" fail"') == False
        assert Validator()._Validator__check_quotes('') == True
        assert Validator()._Validator__check_quotes('"') == False
        assert Validator()._Validator__check_quotes("") == True
        assert Validator()._Validator__check_quotes('"This is a string"') == True
        assert Validator()._Validator__check_quotes('"This" "is" "a" "string"') == True
        assert Validator()._Validator__check_quotes('"This" "is "a" "string"') == False

    def test_end(self):
        assert Validator()._Validator__check_end('Pass.') == True
        assert Validator()._Validator__check_end('Pass?') == True
        assert Validator()._Validator__check_end('Pass!') == True
        assert Validator()._Validator__check_end('Pass!??') == True
        assert Validator()._Validator__check_end('Fail') == False
        assert Validator()._Validator__check_end('Fail,') == False
        assert Validator()._Validator__check_end('Fail! ') == False
        assert Validator()._Validator__check_end('') == False

    def test_punctuation(self):
        assert Validator()._Validator__check_punctuation('Pass.') == True
        assert Validator()._Validator__check_punctuation('Pass?') == True
        assert Validator()._Validator__check_punctuation('Pass!') == True
        assert Validator()._Validator__check_punctuation('.Fail') == False
        assert Validator()._Validator__check_punctuation('Fa.il') == False
        assert Validator()._Validator__check_punctuation('Fa.il.') == False
        assert Validator()._Validator__check_punctuation('Fa.il?') == False
        assert Validator()._Validator__check_punctuation('Fa....il?') == False
        assert Validator()._Validator__check_punctuation('') == True


    def test_numbers(self):
        
        assert Validator()._Validator__check_numbers('check 13 as number') == True
        assert Validator()._Validator__check_numbers('check 10,11,12,13 as number') == False
        assert Validator()._Validator__check_numbers('check 13, 14, 15 as number') == True
        assert Validator()._Validator__check_numbers('check one, two, three as number') == True
        assert Validator()._Validator__check_numbers('check one, 2, three as number') == False
        assert Validator()._Validator__check_numbers('check -1 as number') == False
        assert Validator()._Validator__check_numbers('check minus one as number') == True
        assert Validator()._Validator__check_numbers('check no number') == True
        assert Validator()._Validator__check_numbers('check 13 thirteen as number') == True
        assert Validator()._Validator__check_numbers('') == True

if __name__ == "__main__":
    unittest.main() # run all the tests
