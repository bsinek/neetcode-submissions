class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen_row, seen_col = [], []
        for _ in range(9):
            seen_row.append(set())
            seen_col.append(set())

        seen_3x3 = [[], [], []]
        for r in range(3):
            for c in range(3):
                seen_3x3[r].append(set())

        for r in range(9):
            for c in range(9):
                curr = board[r][c]
                if curr == '.': continue
                if curr in seen_row[r] or curr in seen_col[c]:
                    return False
                grid_idx = (r // 3, c // 3)
                if curr in seen_3x3[grid_idx[0]][grid_idx[1]]:
                    return False
                seen_row[r].add(curr)
                seen_col[c].add(curr)
                seen_3x3[grid_idx[0]][grid_idx[1]].add(curr)
        return True
