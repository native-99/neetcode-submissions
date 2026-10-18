class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        result = 0

        count = {}

        left = 0


        for right in range(len(s)):

            count[s[right]] = count.get(s[right],0)+1

            max_freq = max(count.values())

            length = right - left + 1
            changes = length - max_freq

            while changes > k :
                count[s[left]] -= 1

                left+=1

                max_freq = max(count.values())


                # PENTING: Hitung ulang panjang window
                length = right - left + 1

                # PENTING: Hitung ulang replacements
                changes = length - max_freq

            result = max(result,length)

        return result