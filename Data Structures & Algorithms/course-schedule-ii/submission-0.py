class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        order = [[]]
        for k,v in prerequisites:
            graph[k].append(v)
        UNVISITED = 0
        VISITING = 1
        VISITED = 2

        states = [UNVISITED] * numCourses

        def dfs(i):
            state = states[i]
            if state == VISITED:
                return True
            if state == VISITING:
                return False

            states[i] = VISITING

            for nei in graph[i]:
                if not dfs(nei):
                    return False
            states[i] = VISITED               
            order[0].append(i)
            return True
            

        for course in range(numCourses):
            if not dfs(course):
                return []

        return order[0]    

        