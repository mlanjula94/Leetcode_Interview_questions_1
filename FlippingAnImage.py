class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        FIImage = []
        for lst in A:
            row = []
            for num in lst[::-1]:
                if num == 0:
                    row.append(1)
                else:
                    row.append(0)
            FIImage.append(row)
        return(FIImage)