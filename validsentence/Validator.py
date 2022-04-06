class Validator(object):

    """A class for checking the validity of sentences."""

    # initialisation
    def __init__(self, num=13):
        """allow the user to set the lowest number that can be written with numerals
           defauls to 13 as per requirements otherwise"""

        if not num or not isinstance(num, int):
            self.num_threshold = 13
        else:
            self.num_threshold = num

    def __check_capital(self, string):
        """check the first character is capital, returns True if so"""
        return string[:1].isupper()

    def __check_quotes(self, string):
        """check the string contains an even (or zero) number of double quote characters (")"""
        return (string.count('"') % 2) == 0

    def __check_end(self, string):
        """check the string ends with '.', '!' or '?'"""
        if len(string) == 0:
            return False

        return (string[-1] in '.?!')

    def __check_punctuation(self, string):
        """check there is no '.' before the end of the string"""
        try:
            ind = string.index('.')
            if ind < (len(string)-1):
                return False

            return True
        except ValueError:
            # if the '.' is not found, it cannot be in the wrong place
            return True

    def __check_numbers(self, string):
        """check there are no numeric representations of numbers less than threshold (default 13)"""
        # clean the string by removing commas with spaces (helps splitting the string after)
        clean = string.replace(',', ' ')
        words = clean.split()
        for w in words:
            try:
                if int(w) < self.num_threshold:
                    return False
            except ValueError:
                # any non-number string (ie 'dog') will cause a ValueError when converted to int, ignore these
                pass
        return True

    def validate(self, string):
        """This function checks the given sentence for validity, by taking each check in turn this function
           could be modified to return specific error codes and messages"""

        # check first letter is a capital
        if not self.__check_capital(string):
            return False

        # check even number of quotation marks
        if not self.__check_quotes(string):
            return False

        # check string ends with '.', '?' or '!'
        if not self.__check_end(string):
            return False

        # check no '.' before the last character
        if not self.__check_punctuation(string):
            return False

        # check all numbers below threshold value are spelled out
        if not self.__check_numbers(string):
            return False

        return True
