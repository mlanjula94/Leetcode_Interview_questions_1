class Solution:
    def transpose(self, A: List[List[int]]) -> List[List[int]]:
        #Define variable to save rows the matrix
        matrix = []
        
        for row in range(len(A[0])):
            row_arr = [A[num][row] for num in range(len(A)) ]
            matrix.append(row_arr)
        
        return(matrix)