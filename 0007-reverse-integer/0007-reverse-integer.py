class Solution:
    def reverse(self, x: int) -> int:
        # go to str, reverse using slices, if it's negative make it positive and then negative again
        if x>=0:
            val = int(str(x)[::-1])
        else:
            val = int(str(x*-1)[::-1])*-1
        
        #check for constraints
        if val < -2**31 or val > 2**31-1:
            return 0
        else:
            return val