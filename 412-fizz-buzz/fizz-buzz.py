class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        resultnew=[]
        for i in range(1, n + 1):
            if i % 3 == 0 and i % 5 == 0:
                resultnew.append("FizzBuzz")
            elif i % 3 == 0:
                resultnew.append("Fizz")
            elif i % 5 == 0:
                resultnew.append("Buzz")
            else:
                resultnew.append(str(i))
        return resultnew

         