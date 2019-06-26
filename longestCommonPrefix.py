class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        checker = ""
        prefix = ""
        if not strs:
            return ""
        
        len_arr = min([len(word) for word in strs])
        
        for j in range(len_arr):
            for i in range(len(strs) -1):
                checker = strs[i][j]
                if strs[i][j] != strs[i + 1][j]:
                    checker = ""
            if checker:
                prefix += checker
        return(prefix)
       
                
                