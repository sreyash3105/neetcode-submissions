class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap={}

        count_list=[[] for n in range(len(nums)+1)]#[[] [] [] [] []], for if a list = 6 elemts [111111] saved itself in 6th index 
        return_list=[]# we will later set retun list to be max size = k
        for n in nums:
            hashmap[n]=hashmap.get(n,0)+1 # initialise on unique discovery + 1 counter for current + incoming entries 
        
        for key,val in hashmap.items():
            count_list[val].append(key)
        
        for i in range(len(count_list)-1,0,-1):
            for j in count_list[i]:
                return_list.append(j)
                if k==len(return_list):
                    return return_list
        return []
            
