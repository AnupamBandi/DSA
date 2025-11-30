# https://leetcode.com/problems/maximum-number-of-k-divisible-components/description/?envType=daily-question&envId=2025-11-28

# first solution - longer - DFS
class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        #step 1 : create adjacenecy list from edges

        adj_list = [[] for _ in range(n)]
        for node1,node2 in edges:
            adj_list[node1].append(node2)
            adj_list[node2].append(node1)
        
        #step2: Initialise component count
        component_count = [0]

        #step3: Start DFS traversal from node0

        self.dfs(0,-1,adj_list,values,k,component_count)

        return component_count[0]
    
    def dfs(self,current_node,parent_node,adj_list,node_values,k,component_count):
        #step1: initialise sum for current sub-tree
        sum_ = 0
        #step2: traverse all neighbours

        for neighbor_node in adj_list[current_node]:
            if neighbor_node != parent_node:
                sum_ += self.dfs( neighbor_node,
                    current_node,
                    adj_list,
                    node_values,
                    k,
                    component_count)
                sum_ %= k
        
        sum_ += node_values[current_node]
        sum_ %= k

        if sum_ == 0:
            component_count[0] += 1
        
        return sum_


        
# 2nd solution - easier - DFS

class Solution:
    def MaxKDivisibleComponents(self,n,edges,values,k):
        def dfs(node,parent):
            curSum = values[node]
            for nei in adj_list[node]:
                if nei == parent: continue
                curSum += dfs(nei,node)
            if curSum % k == 0 : self.ans+=1 ; return 0
            return curSum
        adj_list = [[] for _ in range(n)]
        for u,v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)
        self.ans = 0 ; dfs(0,-1)  # semi colon is used to write multiple statements in one line in python  
        return self.ans          
        
       
             