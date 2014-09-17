from FileClass import FileClass
from NodeListClass import NodeList
from TreeNodeClass import TreeNode

__author__  = "Thiago Augustus e Micael Marigo"
__license__ = "GPL"
__version__ = "2.0.0"
__email__   = "thiagoaugustusdeoliveira@gmail.com"
__status__  = "Production"

class Main:

    def __init__(self):

        # Leitura dos arquivos
        chars    = FileClass.getChars("texto.txt")
        nodeList = NodeList.getNodeList(chars)
        treeNode = TreeNode.mount(nodeList)
        print(treeNode,nodeList)
        pass

Main()