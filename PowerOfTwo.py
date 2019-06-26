import math

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 0: return False
    
        return ((n & (n-1)) == 0)
            
        
        #checker = math.log10(n)/math.log10(2)
        #checker_int = int(checker)
        
        #return checker == checker_int