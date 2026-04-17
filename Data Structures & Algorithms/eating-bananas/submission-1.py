class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r = 1,max(piles) 
        res=r
        
        while l<=r:
            mid = l + ((r-l)//2)
            ans=0
            for p in piles:
                ans += math.ceil(p/mid)
            if ans<=h:   
                r=mid-1
                res=mid
            else:
                l=mid+1
        return res



        