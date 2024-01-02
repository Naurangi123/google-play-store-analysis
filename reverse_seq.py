def reverse(S,start,stop):
    if start<stop-1:
        S[start],S[stop-1]=S[stop-1],S[start]
        reverse(S,start+1,stop-1)
    
    


S=[1,2,4,3,5,6,3,47,4]
reverse(S,0,len(S))
print(S)

#by TAil REcursion
def reverse(S):
    start,stop=0,len(S)
    while start<stop-1:
        S[start],S[stop-1]=S[stop-1],S[start]
        start,stop=start+1,stop-1
    
    


S=[1,2,4,3,5,6,3,47,4]
reverse(S)
print(S)


def reverse(S,start,stop):
    if start<stop-1:
        S_list=list(S)
        S_list[start],S_list[stop-1]=S_list[stop-1],S_list[start]

        reverse(S_list,start+1,stop-1)
        S=''.join(S_list)
    return S
    
    


S='naurangi'
S=reverse(S,0,len(S))
print(S)

def reverse_str(s):
    if len(s)==0:
        return s
    else:
        return s[-1]+reverse_str(s[:-1])

strg='naurangi saray'
s=reverse_str(strg)
print(s)