class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        FBArray = []
        
        for n in range( 1, n+1):
            if n % 3 == 0 and n % 5 ==0:
                FBArray.append("FizzBuzz")
            elif n % 3 == 0:
                FBArray.append("Fizz")
            elif n % 5 ==0:
                FBArray.append("Buzz")
            else:
                FBArray.append(str(n))
        
        return(FBArray)