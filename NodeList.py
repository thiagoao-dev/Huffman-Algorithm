import FileClass
from Node import Node


class NodeList:

    nodeList = []

    def __init__(self):

        dict = FileClass.getChars()
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