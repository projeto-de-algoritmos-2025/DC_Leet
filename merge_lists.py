from typing import List, Optional

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        return self._merge_listas(lists, 0, len(lists) - 1)

    def _merge_listas(self, lists: List[Optional[ListNode]], primeiro: int, ultimo: int) -> Optional[ListNode]:
        if primeiro == ultimo:
            return lists[primeiro]

        if primeiro > ultimo:
            return None

        meio = (primeiro + ultimo) // 2

        lista_esquerda_merged = self._merge_listas(lists, primeiro, meio)

        lista_direita_merged = self._merge_listas(lists, meio + 1, ultimo)

        return self._merge_duas_listas(lista_esquerda_merged, lista_direita_merged)

    def _merge_duas_listas(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        raiz = ListNode()
        atual = raiz

        while l1 and l2:
            if l1.val <= l2.val:
                atual.next = l1
                l1 = l1.next
            else:
                atual.next = l2
                l2 = l2.next
            atual = atual.next

        if l1:
            atual.next = l1
        elif l2:
            atual.next = l2

        return raiz.next