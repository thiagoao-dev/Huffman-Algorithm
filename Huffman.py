__author__  = "Thiago Augustus de Oliveira e Douglas Komar"
__license__ = "GPL"
__version__ = "4.3.4"
__email__   = "thiagoaugustusdeoliveira@gmail.com"
__status__  = "Production"

import json


class Huffman:

    pass

class JsonRead:
    def __init__(self):
        pass

    # Read Json Method
    @staticmethod
    def readJson() -> object:
        """
        Return a dictionary
        :rtype : object
        """
        with open("grafod.json") as json_file:
            json_file = json.load(json_file)
            # Test the object
            assert isinstance(json_file, object)
            return json_file

class Counter:

    def __init__(self):
        pass