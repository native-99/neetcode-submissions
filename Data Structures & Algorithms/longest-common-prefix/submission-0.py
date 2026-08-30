class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        first = strs[0]
        longest = ""

        for i in range(1, len(first)+1):
            prefix = first[:i]
            for s in strs[1:]:
                if not s.startswith(prefix):
                    return longest

            longest = prefix

        return longest