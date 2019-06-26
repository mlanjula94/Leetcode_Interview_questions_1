class Solution:
    def reverseWords(self, s: str) -> str:
        return(" ".join(s[::-1].split()[::-1]))
        
        
#First reverse the wholse string so you can get the the reverse of all words.Then split that array by spaces and the reverse again to puth the words in right order.Last join the array 