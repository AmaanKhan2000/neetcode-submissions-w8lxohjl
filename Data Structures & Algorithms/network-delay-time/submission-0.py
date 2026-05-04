class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = collections.defaultdict(list)
        for source,target,time in times:
            graph[source].append((target,time))
        print(graph)   
        visit = set()
        minHeap = [(0,k)]
        t=0
        
        while minHeap:
            timeOne, nodeOne = heapq.heappop(minHeap)
            if nodeOne in visit:
                continue
            visit.add(nodeOne)
            t= max(timeOne,t)
            for nei, neitime in graph[nodeOne]:
                if nei not in visit:
                    heapq.heappush(minHeap, (timeOne + neitime, nei))
        return t if len(visit) == n else -1        
