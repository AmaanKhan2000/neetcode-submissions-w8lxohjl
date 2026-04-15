class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        res = []
        i, j = 0,k

        while i<j:
            temp_arr = []
            for num in range(i,j):
                temp_arr.append(nums[num])
            res.append(max(temp_arr))
            print(i,j)
            if(j==len(nums)):
                break
            i+=1
            j+=1
           
        return res