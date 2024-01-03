def insertion(A):
    for k in range(1,len(A)):
        curr=A[k]
        j=k
        while j>0 and A[j-1]>curr:
            A[j]=A[j-1]
            j-=1
        A[j]=curr
    return A

A=['c','b','c','d','a','e','h','g','f']

result=insertion(A)
print(result)