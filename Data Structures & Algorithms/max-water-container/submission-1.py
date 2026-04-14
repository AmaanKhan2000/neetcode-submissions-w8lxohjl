class Solution:
    def maxArea(self, heights: List[int]) -> int:
        area = 0
        i,j = 0, len(heights)-1

        while i<j:
            if heights[i]<heights[j]:
                if area < heights[i] * (j-i):
                    area = heights[i] * (j-i)
                i+=1
            if heights[i]>heights[j]:
                if area < heights[j] * (j-i):
                    area = heights[j] * (j-i)
                j-=1
            if heights[i] == heights[j]:
                if area < heights[i] * (j-i):
                    area = heights[i] * (j-i)
                i+=1   
        return area        


        