class Solution:
    def isPalindrome(self, s: str) -> bool:
        newS = ""
        
        for l in s:
            if l.isalnum() and l != " ":
                newS += l.lower()
        return(newS == newS[::-1])