from typing import Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        lista_em_ordem = []

        def _em_ordem_traversal(node):
            if node is None:
                return
            _em_ordem_traversal(node.left)
            lista_em_ordem.append(node.val)
            _em_ordem_traversal(node.right)

        _em_ordem_traversal(root)

        def _balancear(primeiro, ultimo):
            if primeiro > ultimo:
                return None

            mid = (primeiro + ultimo) // 2
            raiz = TreeNode(lista_em_ordem[mid])
            raiz.left = _balancear(primeiro, mid - 1)
            raiz.right = _balancear(mid + 1, ultimo)

            return raiz

        return _balancear(0, len(lista_em_ordem) - 1)