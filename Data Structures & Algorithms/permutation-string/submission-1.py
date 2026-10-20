class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        m = len(s1)

        if m > len(s2):
            return False
            
        need = {}

        for c in s1:
            need[c] = need.get(c,0)+1

        window = {}

        for c in s2[:m]:
            window[c] = window.get(c,0)+1

        if need == window:
            return True

        for right in range(m,len(s2)):
            add_char = s2[right]
            window[add_char] = window.get(add_char,0)+1

            remove_char = s2[right-m]
            window[remove_char]-=1

            if window[remove_char] == 0:
                del window[remove_char]

            # Now window represents "id"
            # Compare with {"a":1,"b":1}
            if window == need:
                return True

        return False
