from FileClass import FileClass
from NodeListClass import NodeList
from TreeNodeClass import TreeNode

class Huffman:

    def __init__(self):

        # Leitura dos arquivos
        chars    = FileClass.getChars("texto.txt")
        nodeList = NodeList.getNodeList(chars)
        treeNode = TreeNode.mount(nodeList)
        FileClass.jsonExit(treeNode,nodeList,self.encodeTxt(treeNode))

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