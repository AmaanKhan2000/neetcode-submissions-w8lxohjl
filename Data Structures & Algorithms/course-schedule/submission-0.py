class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_list = defaultdict(list)
        for i,j in prerequisites:
            adj_list[i].append(j)

        UNVISITED = 0
        VISITED = 2
        VISITING = 1

        states = [UNVISITED] * numCourses

        def dfs(node):
            state = states[node]
            if state == VISITED:
                return True
            elif state == VISITING:
                return False

            states[node] = VISITING
            for nei in adj_list[node]:
                if not dfs(nei):
                    return False

            states[node] = VISITED
            return True                
            

        for course in range(numCourses):
            if not dfs(course):
                return False
        return True             
        