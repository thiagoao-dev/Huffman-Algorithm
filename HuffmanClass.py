from FileClass import FileClass
from NodeListClass import NodeList
from TreeNodeClass import TreeNode

class Huffman:

    def __init__(self):

        # Codificar
        chars    = FileClass.getChars("texto.txt")
        nodeList = NodeList.getNodeList(chars)
        treeNode = TreeNode.mount(nodeList)
        FileClass.jsonExit(treeNode,nodeList,self.encodeTxt(treeNode))
        # Decodificar
        chars, code = FileClass.getChars("JsonExit.json")
        nodeList   = NodeList.getNodeList(chars)
        treeNode2   = TreeNode.mount(nodeList)
        print(self.decodeTxt(code,treeNode2))

    def encodeTxt(self,treeNode):
        # Solicita o texto a ser lido
        text = FileClass.readTxt("texto.txt")
        #
        code = ""
        #
        for i in text:
            code += treeNode[0].getCode("",i)
            # Imprime o codigo da letra
            #print(i,mainNode[0].getCode("",i))
        return code

    def decodeTxt(self,code,treeNode):

        text = ""
        while code != None:
            char, code = treeNode[0].getLetter(code)
            text += char
        return text