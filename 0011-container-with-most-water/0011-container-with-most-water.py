class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxCapacity=0
        
        #for start in range(len(height)):
        #    for end in range((len(height)-1), start-1, -1):
        #        capacity=min(height[start], height[end])*(end-start)
        #        if min(height[start], height[end])*(end-start) > maxCapacity:
        #            maxCapacity=capacity

        start, end=0,len(height)-1

        while start<end:
            cap = min(height[start], height[end])*(end-start)

            if cap > maxCapacity:
                maxCapacity = cap
            
            if height[start] < height[end]:
                start+=1
            else:
                end-=1

        return maxCapacity