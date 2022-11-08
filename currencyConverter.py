##https://leetcode.com/discuss/interview-question/483660/Google-or-Phone-or-Currency-Conversion
###graph BFS


from collections import defaultdict
from collections import deque


class CurrencyConvertor():
    def __init__(self, data):
        
        self.data=data
        self.graph_adj_list=defaultdict(list)
        
        ### { 0:[(1,weight1),(2,weight2)],
        ###  1:[(1,weight1),(2,weight2)] }
        
        ##convert to adjacency list
        for node,neighbor,weight in data:
            ##0:[(1,weight1),(2,weight2)]
            self.graph_adj_list[node].append((neighbor,weight))
            self.graph_adj_list[neighbor].append((node,(1.0/weight)))
        
        print(self.graph_adj_list)
    
    def convert_BFS(self,fromCurr,toCurr,amount):
        queue=deque([])
        queue.append((fromCurr,amount))
        visited=set()
        
        while queue:
            curr,currval=queue.popleft()
            if curr in visited:
                continue
            visited.add(curr)
            if curr in self.graph_adj_list:
                neighbors=self.graph_adj_list[curr]
                
                for nei in neighbors:
                    new_cur,convertval=nei
                    if new_cur not in visited:
                        if new_cur==toCurr:
                            return currval*convertval
                        queue.append((new_cur,currval*convertval))
                        
                # next={}
                # for nei in neighbors:
                #     next[nei[0]]=nei[1]
                # for key in next:
                #     if key not in visited:
                #         if key==toCurr:
                #             return currval*next[key]
                #         queue.append((key,currval*next[key]))
            
        
        return -1
        
data = [("USD", "JPY", 110), ("USD", "AUD", 1.45), ("JPY", "GBP", 0.0070),("GBP", "INR",1.2)]
obj1=CurrencyConvertor(data)
print(obj1.convert_BFS("GBP", "AUD",1.0))
