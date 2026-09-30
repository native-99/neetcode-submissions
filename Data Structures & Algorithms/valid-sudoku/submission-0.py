class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = []
        cols = []
        boxes = []

        for i in range(9):
            rows.append(set())
            cols.append(set())
            boxes.append(set())

        for r in range(9):
            for c in range(9):
                num = board[r][c]
                if num == ".":
                    continue
                
                box = (r//3)*3+(c//3)

                if num in rows[r]:
                    return False
                if num in cols[c]:
                    return False
                if num in boxes[box]:
                    return False

                rows[r].add(num)
                cols[c].add(num)
                boxes[box].add(num)

        return True