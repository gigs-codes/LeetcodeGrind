class Solution:
    def pattern5(self, n):
        for i in range(1, n+1):
            for j in range(1, i+1):
                print(i, end="")
            print()

object=Solution()
object.pattern5(n=5)