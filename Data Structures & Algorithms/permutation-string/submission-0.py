class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        need = {}

        for c in s1:
            need[c] = need.get(c,0)+1

        m = len(s1)

        for i in range(len(s2)-m+1):
            window = {}

            for c in s2[i:i+m]:
                window[c] = window.get(c,0)+1

            if window == need:
                return True

        return False