from collections import Counter

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # validate rows
        for row in board:
            nums = [c for c in row if c.isnumeric()]
            counts = Counter(nums)
            has_dupes = any(count for count in counts.values() if count > 1)
            if has_dupes:
                return False

        # validate cols
        transposed = list(zip(*board))
        for col in transposed:
            nums = [c for c in col if c.isnumeric()]
            counts = Counter(nums)
            has_dupes = any(count for count in counts.values() if count > 1)
            if has_dupes:
                return False

        # validate sub grids
        for row_group in range(3):
            for col_group in range(3):
                row_start = row_group * 3
                row_end = row_start + 3
                rows = board[row_start:row_end]
                col_start = col_group * 3
                col_end = col_start + 3
                nums = []
                for row in rows:
                    cols = row[col_start:col_end]
                    nums = nums + [col for col in cols if col.isnumeric()]
                counts = Counter(nums)
                has_dupes = any(count for count in counts.values() if count > 1)
                if has_dupes:
                    return False
        return True