class solution:
    def pattern(self, n):
        i=1
        j=1
        for i in range(1,n+1):
            for j in range(1,i+1):
                print(j, end="")
            print()
        

object = solution()
object.pattern(5)