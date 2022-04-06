import unittest
from validsentence.Validator import Validator

class FullSentenceTest(unittest.TestCase):

    def setUp(self):
        """Call before every test."""
        self.validator = Validator()

    def test_empty_sentence(self):
        assert self.validator.validate('') == False
    
    def test_valid_sentence_1(self):
        assert self.validator.validate('The quick brown fox said "hello Mr lazy dog".') == True

    def test_valid_sentence_2(self):
        assert self.validator.validate('The quick brown fox said hello Mr lazy dog.') == True

    def test_valid_sentence_3(self):
        assert self.validator.validate('One lazy dog is too few, 13 is too many.') == True

    def test_valid_sentence_4(self):
        assert self.validator.validate('One lazy dog is too few, thirteen is too many.') == True

    def test_valid_sentence_5(self):
        assert self.validator.validate('How many "lazy dogs" are there?') == True

    def test_invalid_sentence_1(self):
        """Full stop in middle of sentence"""
        assert self.validator.validate('The quick brown fox said "hello Mr. lazy dog".') == False

    def test_invalid_sentence_2(self):
        """Sentence starts with lower case character"""
        assert self.validator.validate('the quick brown fox said "hello Mr lazy dog".') == False

    def test_invalid_sentence_3(self):
        """Sentence contains 3 double quotes"""
        assert self.validator.validate('"The quick brown fox said "hello Mr lazy dog."') == False

    def test_invalid_sentence_4(self):
        """Number less than 13 not written out"""
        assert self.validator.validate('One lazy dog is too few, 12 is too many.') == False

    def test_invalid_sentence_5(self):
        """Number less than 13 not written out"""
        assert self.validator.validate('Are there 11, 12 or 13 lazy dogs?') == False

    def test_invalid_sentence_6(self):
        """Sentence does not end in a '.', '?' or '!'"""
        assert self.validator.validate('There is no punctuation in this sentence') == False

if __name__ == "__main__":
    unittest.main() # run all the tests
