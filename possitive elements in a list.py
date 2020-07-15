i=0
j=1
list1=[]
list2=[]
n=int(input("Enter the number of elements in the list :"))
print("Enter the elements of the list :")
while(j<=n):
    a=int(input())
    list1.append(a)
    j=j+1
while(i<=n):
    if list1[i] >= 0:
        print("[",list1[i], end = " ]")
    i=i+1    
        
