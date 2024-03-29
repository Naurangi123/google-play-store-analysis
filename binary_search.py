def binary_search(data,target,low ,high):

    if low>high:
        return False
    else:
        mid=(low+high)//2
        if target==data[mid]:
            return target
        elif target<data[mid]:
            return binary_search(data,target,low,mid-1)
        else:
            return binary_search(data,target,mid+1,high)
        

data=[2,4,5,7,8,9,12,14,17,19,22,25,27,28,33,37]
result=binary_search(data,target=22,low=0,high=len(data)-1)
print(result)


def binary_search(data,target):

    low=0
    high=len(data)-1
    while low<=high:
        mid=(low+high)//2
        if target==data[mid]:
            return target
        elif target<data[mid]:
            high=mid-1
        else:
            low=mid+1
    return False

data=[2,4,5,7,8,9,12,14,17,19,22,25,27,28,33,37]
s=binary_search(data,target=28)
print(s)
        

