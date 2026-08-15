"""To take input"""
num=int(input("Enter the number of elements you want to input : "))
"""variables"""
arr2=[]
arr2=[]
c=0
"""Inputing list"""
for i in range(num):
    arr2.append((input()))
n=len(arr2)
"""Sorting the list"""
for i in range(n):
    for j in range(0,n-i-1):
        if arr2[j]>arr2[j+1]:
            temp=arr2[j]
            arr2[j]=arr2[j+1]
            arr2[j+1]=temp
"""Removing the duplicate"""
for i in range(len(arr2)):
    for j in range(i+1,len(arr2)):
        if arr2[i]==arr2[j]:
            arr2[j]="-"
arr3=[]
for i in range(len(arr2)):
    if arr2[i] != "-":
        arr3.append(arr2[i])
    else:
        c+=1
print(arr3)
"""Finding the second largest number and if it dosen't exist it will writen -1"""
for i in range(len(arr3)):
    if arr3[len(arr3)-2]==arr3[i]:
        c=c+1
    else:
        continue
if c==n:
    print("-1")
else:
    print("your second largest number is : ",arr3[len(arr3)-2])