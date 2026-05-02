class Solution(object):
    def removeElement(self, nums, val):
        k = 0
        for i in range(len(nums)):
            if(nums[i]!=val):
                nums[k]=nums[i]
                k=k+1
        
        return k
    
def main():
        nums = [1,2,3,3,0]
        val = 3

        sol=Solution()
        k=sol.removeElement(nums, val)

        print("k = ", k)
        print("updated nums[] ", nums[:k])

if __name__=="__main__":
    main()