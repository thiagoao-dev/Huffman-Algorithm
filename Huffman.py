__author__  = "Thiago Augustus de Oliveira"
__license__ = "GPL"
__version__ = "1.0.0"
__email__   = "thiagoaugustusdeoliveira@gmail.com"
__status__  = "Production"

import json


class Huffman:

    def __init__(self):
        NodeList()

class NodeList:

    nodeList = []

    def __init__(self):

        dict = TextCount().counterLetter
        total = dict.pop('total')

        for i in dict:
            self.nodeList.append(
                Node(
                    i, round(
                        (
                            (dict[i]*100) / total
                        )
                    )
                )
            )
        print(self.nodeList)

class Node:

    value = None
    node_0 = None
    node_1 = None
    percent = None

    def __init__(self, v, p):
        self.value   = v
        self.percent = p

class TxtRead:

    @property
    def readFile(self: object) -> object:
        # Abre e Lê o arquivo texto.txt
        txt_file = open("texto.txt", "rt")
        txt = txt_file.read()

        # Transforma todas as quebras de linhas em espaço simples
        txt = txt.replace("\n", " ")

        #
        return txt

class JsonRead:

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

class TextCount:

    letters = {}

    @property
    def counterLetter(self: object) -> object:

        # Solicita o texto a ser lido
        text = TxtRead().readFile

        readed = []
        total  = 0

        # Varre todo o texto, caracter por caracter
        for i in range(len(text)):

            #
            total += 1

            # Caso o caracter ainda não tenha sido lida
            if text[i] not in readed:

                # Add o caracter aos lidos e add ao dicionario
                readed.append(text[i])
                self.letters[text[i]] = 1
            #
            else:

                # Soma 1 ao caracter já adcionado
                self.letters[text[i]] += 1

        #
        self.letters['total'] = total

        # Retorna um dicionario com os caracteres nos indices e totais
        return self.letters

Huffman()