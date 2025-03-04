class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        _5 = 0
        _10 = 0
        _20 = 0
        
        for num in bills:
            if num == 5:
                _5 += 1
            elif num == 10:
                _10 += 1
            elif num == 20:
                _20 += 1
                
            if num == 10 and _5 != 0:
                _5 -= 1
            elif num == 20:
                if _5 >= 1 and _10 >= 1:
                    _5 -= 1
                    _10 -= 1
                elif _5 >= 3:
                    _5 -=3
                else:
                    return False
            elif num != 5:
                return False
        return True

