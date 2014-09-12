import copy

__author__  = "Thiago Augustus de Oliveira e Micael Marigo"
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

        mainNode = self.treeTxtMount()
        encode   = self.textEncoding(mainNode)
        self.mountExit(mainNode, encode, 'toJson')

        #tree     = JsonRead.readJson()['tree']
        #print(tree['nodes'])
        #decode   = JsonRead.readJson()['string']
        #self.mountExit(mainNode, JsonRead.readJson()['string'], 'toText')

    def mountExit(self, node = None, code = '', type = 'toJson'):
        #
        if type == 'toJson':

            # Esqueleto do arquivo de saida
            exit = {
                "tree": {
                    "nodes": []
                },
                "string": ""
            }

            # Recupera a lista de nos
            nodeList = NodeList().getNodeList

            # Recupera a contagem de caracter do texto original
            textCount = TextCount().counterLetter()

            # Atribui o arquivo codificado a saida
            exit["string"] = code

            # Atribui os caracteres, quantidade e peso
            for i in nodeList:
                # Verifica se o no e valido
                if i.getValue != None:
                    exit["tree"]["nodes"].append([i.getValue, textCount[i.getValue], i.getPercent, node[0].getCode("",i.getValue)])

            # Escreve no arquivo
            file = open("JsonExit.json", "w")
            json.dump(exit, file)
            file.close()

        #
        elif type == 'toText':

            # Escreve no arquivo
            file = open("TxtExit.txt", "w")
            #file.write(str(exit))
            file.close()

    def textEncoding(self, mainNode):

        # Solicita o texto a ser lido
        text = TxtRead().readFile
        #
        code = ""
        #
        for i in text:
            code += mainNode[0].getCode("",i)
            # Imprime o c?digo da letra
            #print(i,mainNode[0].getCode("",i))

        return code

    def treeTxtMount(self):

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

    def treeJsonMount(self):

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
    def getValue(self):
        return self.value

    @property
    def getPercent(self):
        if self.node_0 == None:
            return self.percent
        else:
            return (self.node_0.getPercent + self.node_1.getPercent)

    def getCode(self, pos, char):
        # Caso aja nos filhos
        if self.node_0 != None:
            # Retorna o codigo do no filho
            return self.node_0.getCode(pos+"0",char)+self.node_1.getCode(pos+"1",char)
        # Caso o char seja encontrado
        elif self.value == char:
            # Retorna a posicao
            return pos
        # Caso nao encontrado
        else:
            # Retorna nada
            return ""

class NodeList:

    nodeList = []

    def __init__(self):

        dict = TextCount().counterLetter()
        total = dict.pop('total')
        #
        for i in dict:
            self.nodeList.append(
                Node(
                    round(
                        (
                            ((dict[i]*100) / total) / 100
                        ),
                        3 # Total de casas apos a virgula
                    )
                ).setValue(i)
            )

    @property
    def getNodeList(self):
        #
        return self.nodeList

class TextCount:

    letters = {}

    def counterLetter(self: object, type = 'txt') -> object:

        if type == 'txt':
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

        textJ = JsonRead().readJson
        print(textJ['tree']['nodes'])
        textE = []


        print(self.letters)
        # Retorna um dicionario com os caracteres nos indices e totais
        return self.letters

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
    @property
    def readJson(self: object) -> object:
        """
        Return a dictionary
        :rtype : object
        """
        with open("texto-descomp.json") as json_file:
            json_file = json.load(json_file)
            # Test the object
            assert isinstance(json_file, object)
            return json_file

# ------------------- MAIN -------------------
Huffman()