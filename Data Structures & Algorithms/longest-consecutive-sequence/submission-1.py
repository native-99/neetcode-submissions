class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
                return 0

        arr = sorted(nums)

        longest = 1
        length = 1

        for i in range(1, len(arr)):
            if arr[i] == arr[i - 1]:
                continue

            if arr[i] == arr[i - 1] + 1:
                length += 1
            else:
                length = 1

            longest = max(longest, length)

        return longest