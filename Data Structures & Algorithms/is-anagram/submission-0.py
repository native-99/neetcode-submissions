class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        t_list = list(t)

        for char in s:
            if char not in t_list:
                return False
            t_list.remove(char)
        return True