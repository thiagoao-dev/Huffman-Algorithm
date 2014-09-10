import copy

__author__  = "Thiago Augustus de Oliveira"
__license__ = "GPL"
__version__ = "1.0.0"
__email__   = "thiagoaugustusdeoliveira@gmail.com"
__status__  = "Production"

import json


class Huffman:

    node_0 = None
    node_1 = None
    nodeIndex_0 = -1
    nodeIndex_1 = -1

    def __init__(self):

        lastNode = self.treeMount()
        self.textCoding(lastNode)

    def textCoding(self, mainNode):

        # Solicita o texto a ser lido
        text = TxtRead().readFile

        coding = None

        for i in text:
            print(i,mainNode[0].getCode("",i))

        print(text)

    def treeMount(self):

        # Inicia os nos menores
        self.node_0 = Node(float('inf'))
        self.node_1 = Node(float('inf'))

        nodeList = NodeList().getNodeList

        # Enquanto a lista conter mais de um no
        while len(nodeList) > 1:

            # Cria um lista copia da lista original
            cp = copy.copy(nodeList)

            # Enquanto houve nos na lista copia
            while cp:

                # Remove o no da ponta
                node = cp.pop()

                # Caso o seja o com menor percentual
                if node.getPercent < self.node_0.percent:
                    #
                    self.node_1 = self.node_0
                    self.nodeIndex_1 = self.nodeIndex_0

                    #
                    self.node_0 = node
                    self.nodeIndex_0 = len(cp)
                #
                elif node.getPercent < self.node_1.percent:
                    #
                    self.node_1 = node
                    self.nodeIndex_1 = len(cp)

            # --- GAMBIARRA ---
            for i in nodeList:
                if i == self.node_0:
                    nodeList.remove(i)
                if i == self.node_1:
                    nodeList.remove(i)

            for i in nodeList:
                if i == self.node_0:
                    nodeList.remove(i)
                if i == self.node_1:
                    nodeList.remove(i)
            # --- FIM GAMBIARRA ---

            # Adiciona novo no a lista
            nodeList.append(
                Node(
                    self.node_0.getPercent +
                    self.node_1.getPercent
                ).setNode(
                    self.node_0,self.node_1
                )
            )

            # Reinicia os nos menores
            self.node_0 = Node(float('inf'))
            self.node_1 = Node(float('inf'))

        #
        return nodeList

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

    def getCode(self, pos, char):
        if self.node_0 != None:
            return self.node_0.getCode(pos+"0",char)+self.node_1.getCode(pos+"1",char)
        elif self.value == char:
            return pos
        else:
            return ""

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
                        3 # Total de casas apos a virgula
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
        # Abre e L? o arquivo texto.txt
        txt_file = open("texto.txt", "rt")
        txt = txt_file.read()

        # Transforma todas as quebras de linhas em espa?o simples
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

            # Caso o caracter ainda nao tenha sido lida
            if text[i] not in readed:

                # Add o caracter aos lidos e add ao dicionario
                readed.append(text[i])
                self.letters[text[i]] = 1
            #
            else:

                # Soma 1 ao caracter ja adcionado
                self.letters[text[i]] += 1

        #
        self.letters['total'] = total

        # Retorna um dicionario com os caracteres nos indices e totais
        return self.letters

Huffman()