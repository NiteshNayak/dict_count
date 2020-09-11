# There is a robot starting at position (0, 0), the origin, on a 2D plane. Given a sequence of its moves, judge if this robot ends up at (0, 0) after it completes its moves.

class Solution:
    def judgeCircle(self, moves: str) -> bool:
        x = 0
        y = 0
        for i in moves:
            if i is "U":
                y = y + 1
            if i is "D":
                y = y - 1
            if i is "L":
                x = x - 1
            if i is "R":
                x = x + 1
        
        if x == 0 and y == 0:
            return True
        else:
            return False
