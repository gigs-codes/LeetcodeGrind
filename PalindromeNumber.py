class PalindromeNumber(object):
    def isPalindrome(self,x):
        if (x<0):
            return False
        
        original=x
        rev=0

        while (x>0):
            digit=x%10
            rev=rev*10+digit
            x=x//10
        
        return original == rev
    
if __name__=="__main__":
    x=int(input("enter the number :  "))

    sol=PalindromeNumber()
    result=sol.isPalindrome(x)

    print(result)