class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        sol = []
        for i, num1 in enumerate(nums[0:len(nums)-1]):
            for _, num2 in enumerate(nums[i+1:len(nums)]):
                if target == num1 + num2 :
                    sol.append(i)
                    sol.append(i+1)
                    return print(sol)
        print("{} not found in the list".format(target))

obj = Solution()
obj.twoSum([2,7,11,15], 18)
