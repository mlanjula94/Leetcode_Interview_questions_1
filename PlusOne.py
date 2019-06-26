class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        StringNums = [str(l) for l in digits]
        DPArr = [int(num) for num in str(int("".join(StringNums)) + 1)]
        return(DPArr) 