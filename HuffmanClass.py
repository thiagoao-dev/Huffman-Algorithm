from FileClass import FileClass
from NodeListClass import NodeList
from TreeNodeClass import TreeNode

class Huffman:

    def __init__(self):

        # Codifica
        chars    = FileClass.getChars("texto.txt")
        nodeList = NodeList.getNodeList(chars)
        treeNode = TreeNode.mount(nodeList)
        FileClass.jsonExit(treeNode,nodeList,self.encodeTxt(treeNode))

        # Decodifica
        chars, code = FileClass.getChars("JsonExit.json")
        nodeList    = NodeList.getNodeList(chars)
        treeNode2   = TreeNode.mount(nodeList)
        text        = self.decodeTxt(code,treeNode2)
        FileClass.textExit(text)

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
        #
        text = ""
        # Enquanto o tamanho remanescente do codigo for maior que zero
        while len(code) > 0:
            # Resgata a letra a partir do no raiz e codigo remanescente
            char, code = treeNode[0].getLetter(code)
            # Monta o texto
            text += char
        return text