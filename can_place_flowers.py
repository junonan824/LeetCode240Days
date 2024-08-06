class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        for i in range(len(flowerbed)):
            if n == 0:
                return True
            if flowerbed[i] == 0:
                left_empty = (i == 0) or (flowerbed[i - 1] == 0)
                right_empty = (i == len(flowerbed) - 1) or (flowerbed[i + 1] == 0)

                if left_empty and right_empty:
                    flowerbed[i] = 1
                    n -= 1
        return n == 0

# Test case execution
if __name__ == "__main__":
    sol = Solution()
    # Test case: Can Place Flowers
    assert sol.canPlaceFlowers([1, 0, 0, 0, 1], 1) == True
    assert sol.canPlaceFlowers([1, 0, 0, 0, 1], 2) == False
    assert sol.canPlaceFlowers([0, 0, 1, 0, 0], 1) == True
    assert sol.canPlaceFlowers([0, 0, 1, 0, 0], 2) == True

    print("All tests for Can Place Flowers passed.")