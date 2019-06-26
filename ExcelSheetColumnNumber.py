def ltrIndex(s):
    return(ord(s)-64)

class Solution:
    def titleToNumber(self, s: str) -> int:
        column = 0
        counter = 0
        
        #if len(s) == 0:
         #   column =  ltrIndex(s[i])
        
        s_rev = s[::-1]
        for i in range(len(s_rev)):
            column += ((26**counter)*ltrIndex(s_rev[i])) 
            counter += 1
        return(column)