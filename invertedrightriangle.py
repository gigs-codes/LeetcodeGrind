class Solution:
    def pattern(self, n):
        for i in range(n):
            for j in range(n-i):
                print("*",end="")
            print()

object = Solution()
object.pattern(n=5)