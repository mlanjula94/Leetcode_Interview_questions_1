class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        #declare arrays to save odds and evens
        even = []
        odd = []
        
        #Fill the arrays with odd array with odd numbers and evens with Evens
        for num in A:
            if num%2 == 0:
                even.append(num)
            else:
                odd.append(num)
                
        #Concat the two arrays
        return(even+odd)