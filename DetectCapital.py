class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if word.upper() == word:
            return True
        elif word.lower() == word:
            return True
        elif word[0].upper() + word[1:].lower() == word:
            return True
        else:
            return False