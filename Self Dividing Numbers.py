class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        numbers = range(left,right+1)
        num_arr = [list(str(num)) for num in range(left,right+1)]
        SDArray = []
        
        for number in range(len(numbers)):
            self_divide = 1
            for digit in num_arr[number]:
                if int(digit) == 0:
                    self_divide = 0
                elif  numbers[number] % int(digit) != 0:
                    self_divide = 0
            if self_divide == 1:
                SDArray.append(numbers[number])
        return(SDArray)