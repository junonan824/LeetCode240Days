class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        max_num = max(candies)
        result = []
        for candy in candies:
            result.append(candy + extraCandies >= max_num)
        return result

# Test case execution
if __name__ == "__main__":
    sol = Solution()

    # Test case: Kids With the Greatest Number of Candies
    assert sol.kidsWithCandies([2, 3, 5, 1, 3], 3) == [True, True, True, False, True]
    assert sol.kidsWithCandies([4, 2, 1, 1, 2], 1) == [True, False, False, False, False]
    assert sol.kidsWithCandies([12, 1, 12], 10) == [True, False, True]

    print("All tests for Kids With the Greatest Number of Candies passed.")