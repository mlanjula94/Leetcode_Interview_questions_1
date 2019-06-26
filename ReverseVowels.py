class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = []
        
        for letter in s:
            if letter.lower() in ('a','e', 'i', 'o', 'u'):
                vowels.insert(0,letter)
                s = s.replace(letter,"_")
        
        for l in s:
            if l == "_":
                s = s.replace("_", vowels[0], 1)
                vowels.pop(0)
        return(s)
                