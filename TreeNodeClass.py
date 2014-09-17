import copy
from NodeClass import Node
from NodeListClass import NodeList


class TreeNode:

    node_0 = None
    node_1 = None
    nodeIndex_0 = -1
    nodeIndex_1 = -1

    @staticmethod
    def mount(nodeList):

        nodeListTemp = copy.deepcopy(nodeList)

        # Inicia os nos menores
        TreeNode.node_0 = Node(float('inf'))
        TreeNode.node_1 = Node(float('inf'))

        # Enquanto a lista conter mais de um no
        while len(nodeListTemp) > 1:
            # Cria um lista copia da lista original
            cp = copy.copy(nodeListTemp)

            # Enquanto houve nos na lista copia
            while cp:

                # Remove o no da ponta
                node = cp.pop()

                # Caso o seja o com menor percentual
                if node.getPercent < TreeNode.node_0.percent:
                    #
                    TreeNode.node_1 = TreeNode.node_0
                    TreeNode.nodeIndex_1 = TreeNode.nodeIndex_0

                    #
                    TreeNode.node_0 = node
                    TreeNode.nodeIndex_0 = len(cp)
                #
                elif node.getPercent < TreeNode.node_1.percent:
                    #
                    TreeNode.node_1 = node
                    TreeNode.nodeIndex_1 = len(cp)

            # --- GAMBIARRA ---
            for i in nodeListTemp:
                if i == TreeNode.node_0:
                    nodeListTemp.remove(i)
                if i == TreeNode.node_1:
                    nodeListTemp.remove(i)

            for i in nodeListTemp:
                if i == TreeNode.node_0:
                    nodeListTemp.remove(i)
                if i == TreeNode.node_1:
                    nodeListTemp.remove(i)
            # --- FIM GAMBIARRA ---

            # Adiciona novo no a lista
            nodeListTemp.append(
                Node(
                    TreeNode.node_0.getPercent +
                    TreeNode.node_1.getPercent
                ).setNode(
                    TreeNode.node_0,TreeNode.node_1
                )
            )

            # Reinicia os nos menores
            TreeNode.node_0 = Node(float('inf'))
            TreeNode.node_1 = Node(float('inf'))

        return nodeListTemp