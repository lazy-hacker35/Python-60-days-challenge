class Solution(object):
   def twoSum(self, num, target):
    hashmap = {}
    for i in range(len(num)):
        complement = target - num[i]
        if complement in hashmap:
            return [hashmap[complement], i]
        hashmap[num[i]] = i
    return []
print(Solution().twoSum(num=[2,7,11,15], target=13))
#print(Solution().twoSum(num=[3,2,4], target=6))
#print(Solution().twoSum(num=[3,3], target=6))
#print(Solution().twoSum(num=[1,2,3,4,5], target=10))
#print(Solution().twoSum(num=[0,4,3,0], target=0))
#print(Solution().twoSum(num=[-3,4,3,90], target=0)) 