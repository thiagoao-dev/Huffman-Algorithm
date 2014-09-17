from NodeClass import Node

class NodeList:

    nodeList = []

    @staticmethod
    def getNodeList(chars):

        if len(NodeList.nodeList) > 0:
            NodeList.nodeList = []

        for i in chars:

            node = Node(i[2]).setValue(i[0]).setCount(i[1])
            NodeList.nodeList.append(node)

        return NodeList.nodeList