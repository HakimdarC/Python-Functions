def max_2(a,b):
    if a<b:
        return b
    else:
        return a

def max(a,b,c):
    if max_2(a,b)<c:
        return c
    else:
        return max_2(a,b)

print(max(3,55,6))


            
    
