class removeduplicate(object):
    def removeDuplicates(self, nums):
        if len(nums) == 0:
            return 0

        k = 1

        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                nums[k] = nums[i]
                k += 1

        return k
    

if __name__=="__main__":
    nums=[1,1,5,6,7,9,1,1,0,0]
    dupli=removeduplicate()
    result=dupli.removeDuplicates(nums)

    print(result)