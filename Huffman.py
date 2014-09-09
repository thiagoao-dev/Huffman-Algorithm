<<<<<<< HEAD
__author__  = "Thiago Augustus de Oliveira"
__license__ = "GPL"
__version__ = "1.0.0"
=======
__author__  = "Thiago Augustus de Oliveira e Douglas Komar"
__license__ = "GPL"
__version__ = "4.3.4"
>>>>>>> origin/master
__email__   = "thiagoaugustusdeoliveira@gmail.com"
__status__  = "Production"

import json


class Huffman:
<<<<<<< HEAD
    pass

class TxtRead:

    def __init__(self):
        return None

    @property
    def readFile(self: object) -> object:
        txt_file = open("texto.txt", "rt")
        txt = txt_file.read()
        txt = txt.replace("\n", " ")
        return txt
=======

    pass
>>>>>>> origin/master

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

<<<<<<< HEAD
    letters = {}
    readed  = []

    def __init__(self):
        pass

    def counterLetter(self):
        text = TxtRead().readFile
        for i in range(len(text)):
            if text[i] not in self.readed:
                self.readed.append(text[i])
                self.letters[text[i]] = 1
            else:
                self.letters[text[i]] += 1

        print(self.letters)


print(Counter().counterLetter())
=======
    def __init__(self):
        pass
>>>>>>> origin/master
