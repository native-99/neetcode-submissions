class Solution:
    def findMedianSortedArrays(self, nums1, nums2):

        A, B = nums1, nums2

        # Binary Search pada array yang lebih pendek
        if len(A) > len(B):
            A, B = B, A

        m, n = len(A), len(B)

        # Jumlah angka yang harus ada di kiri
        half = (m + n + 1) // 2

        left = 0
        right = m

        while left <= right:

            # Tentukan jumlah elemen kiri A
            i = (left + right) // 2

            # Sisanya harus dari B
            j = half - i

            # Ambil empat angka di sekitar partition
            Aleft = A[i - 1] if i > 0 else float("-inf")
            Aright = A[i] if i < m else float("inf")

            Bleft = B[j - 1] if j > 0 else float("-inf")
            Bright = B[j] if j < n else float("inf")

            # Partition sudah benar
            if Aleft <= Bright and Bleft <= Aright:

                # Total ganjil
                if (m + n) % 2 == 1:
                    return float(max(Aleft, Bleft))

                # Total genap
                else:
                    return (
                        max(Aleft, Bleft) +
                        min(Aright, Bright)
                    ) / 2

            # Aleft terlalu besar, geser kiri
            elif Aleft > Bright:
                right = i - 1

            # Bleft terlalu besar, geser kanan
            else:
                left = i + 1