from typing import List

class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        # Função principal que chama o método de contagem
        return self.sort_and_count(nums, 0, len(nums) - 1)
    
    def sort_and_count(self, nums: List[int], left: int, right: int) -> int:
        if left >= right:
            return 0
        
        mid = (left + right) // 2
        # Conta pares nas metades esquerda e direita
        count = self.sort_and_count(nums, left, mid) + self.sort_and_count(nums, mid + 1, right)
        
        # Conta pares entre as metades
        j = mid + 1
        for i in range(left, mid + 1):
            while j <= right and nums[i] > 2 * nums[j]:
                j += 1
            count += j - (mid + 1)
        
        # Mescla as metades ordenadas (usando sorted para simplificar)
        nums[left:right + 1] = sorted(nums[left:right + 1])
        return count