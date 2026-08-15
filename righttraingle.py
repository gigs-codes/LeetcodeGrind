#*
#**
#***
#****

class Solution:
    def pattern(self, n):
        
        for i in range(n):
            for j in range(i+1):
                print("*", end=(""))
            print()

object = Solution()
object.pattern(4)