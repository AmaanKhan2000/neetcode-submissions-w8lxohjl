class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        temp_ds = []
        res = []
        n=len(nums)
        def bt(index, diff, temp_ds):
            if index == n:
                if diff == 0:
                    res.append(temp_ds.copy())
                return
            if nums[index] <=diff:
                temp_ds.append(nums[index])
                bt(index,diff-nums[index],temp_ds)
                temp_ds.pop()
            bt(index+1,diff,temp_ds)
        bt(0,target,temp_ds)
        return res
             
                    
        