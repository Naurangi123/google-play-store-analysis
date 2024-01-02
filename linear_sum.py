def linear_sum(S,n):
    if n==0:
        return 0
    else:
        return linear_sum(S,n-1)+S[n-1]
    
S=[4,3,6,2,8,5,8,9,4,4,2,11,3,5,7,9,5,3,4]
result=linear_sum(S,len(S))
print(result)