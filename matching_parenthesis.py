def is_matched(expr):
    left='({['
    right=')}]'
    S=[]
    for c in expr:
        if c in left:
            S.append(c)
        elif c in right:
            if not S:
                return False
            if right.index(c)!=left.index(S.pop()):
                return False
    return not S

expr='((( )(( )){([( )])}))'
result=is_matched(expr)
print(result)