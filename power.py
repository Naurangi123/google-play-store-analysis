def power(x,n):
    if n==0:
        return 1
    else:
        return x*power(x,n-1)
    
print(power(5,2))


def powr(x,n):
    if n==0:
        return 1
    else:
        partial=power(x,n//2)
        result=partial*partial
        if n%2==1:
            result*=x
        return result
print(powr(2,13))