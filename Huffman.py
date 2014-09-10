import copy

__author__  = "Thiago Augustus de Oliveira"
__license__ = "GPL"
__version__ = "1.0.0"
__email__   = "thiagoaugustusdeoliveira@gmail.com"
__status__  = "Production"

import json


class Huffman:

    node_0 = None
    nodeIndex_0 = -1
    node_1 = None
    nodeIndex_1 = -1
    nodeTree = None

    def __init__(self):

        self.node_0 = Node(float('inf'))
        self.node_1 = Node(float('inf'))

        nodeList = NodeList().getNodeList

        while len(nodeList) > 1:
            #
            cp = copy.copy(nodeList)
            while cp:
                #
                node = cp.pop()
                #
                if node.getPercent < self.node_0.percent:
                    self.node_1 = self.node_0
                    self.nodeIndex_1 = self.nodeIndex_0

                    self.node_0 = node
                    self.nodeIndex_0 = len(cp)
                elif node.getPercent < self.node_1.percent:
                    self.node_1 = node
                    self.nodeIndex_1 = len(cp)
            #

            # O POP TÁ ERRADO
            nodeList.pop(self.nodeIndex_0)
            nodeList.pop(self.nodeIndex_1-1)

            nodeList.append(
                Node(
                    self.node_0.getPercent +
                    self.node_1.getPercent
                ).setNode(
                    self.node_0,self.node_1
                )
            )
            #
            self.node_0 = Node(float('inf'))
            self.node_1 = Node(float('inf'))
        print(nodeList[0].getPercent)

class Node:

    value = None
    node_0 = None
    node_1 = None
    percent = None

    def __init__(self, p):
        self.percent = p

    def setValue(self, v):
        self.value = v
        return self

    def setNode(self, node_0, node_1):
        if self.node_0 == None and self.node_1 == None:
            self.node_0 = node_0
            self.node_1 = node_1
        return self

    @property
    def getPercent(self):
        if self.node_0 == None:
            return self.percent
        else:
            return (self.node_0.getPercent + self.node_1.getPercent)

class NodeList:

    nodeList = []

    def __init__(self):

        dict = TextCount().counterLetter
        total = dict.pop('total')

        #
        for i in dict:
            self.nodeList.append(
                Node(
                    round(
                        (
                            (dict[i]*100) / total
                        ),
                        3 # Total de casas após a virgula
                    )
                ).setValue(i)
            )

    @property
    def getNodeList(self):
        #
        return self.nodeList

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