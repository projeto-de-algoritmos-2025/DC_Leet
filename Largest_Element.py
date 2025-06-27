import random
from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def quickselect(left, right, k_smallest):
            # Escolhe um pivô aleatório e particiona o array
            pivot_index = random.randint(left, right)
            nums[right], nums[pivot_index] = nums[pivot_index], nums[right]
            pivot = nums[right]
            i = left
            
            for j in range(left, right):
                if nums[j] <= pivot:
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1
            
            nums[i], nums[right] = nums[right], nums[i]
            
            # Verifica se o pivô está na posição correta
            if k_smallest == i:
                return nums[i]
            elif k_smallest < i:
                return quickselect(left, i - 1, k_smallest)
            else:
                return quickselect(i + 1, right, k_smallest)
        
        # k-ésimo maior elemento é o (n - k)-ésimo menor elemento
        return quickselect(0, len(nums) - 1, len(nums) - k)