class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def bt(index, summ, temp):
            if summ == target:
                res.append(temp.copy())
                return
            for i in range(index, len(candidates)):
                if i>index and candidates[i] == candidates[i-1]:
                    continue
                if summ + candidates[i] > target:
                    break
                temp.append(candidates[i])
                bt(i+1, summ + candidates[i], temp)
                temp.pop()

        bt(0,0,[])
        return res
        