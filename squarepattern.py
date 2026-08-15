class Solution:
    def pattern1(self, n):
        for i in range(4):
            for j in range(4):
                print("*", end="")
            print()
        
object = Solution()
object.pattern1(4)
    