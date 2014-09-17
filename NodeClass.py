class Node:

    value   = None
    percent = None
    count   = 0
    node_0  = None
    node_1  = None

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

    def setCount(self, t):
        self.count = t
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

    @property
    def getCount(self):
        return self.count