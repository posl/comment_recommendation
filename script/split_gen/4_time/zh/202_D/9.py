def get_num(a,b,k):
    if a==0:
        return "b"*b
    if b==0:
        return "a"*a
    if k<=0:
        return "a"*a+"b"*b
    if a==1 and b==1:
        return "ab"
    if a==1 and b==2:
        return "abb"
    if a==2 and b==1:
        return "aab"
    if a==1:
        return "ab"+"a"*(b-2)+"b"
    if b==1:
        return "ba"+"b"*(a-2)+"a"
    if k==1:
        return "a"*a+"b"*b
    elif k==2:
        return "ab"+"a"*(b-1)+"b"*(a-1)
    elif k==3:
        return "ba"+"b"*(a-1)+"a"*(b-1)
    elif k==4:
        return "aab"+"a"*(b-2)+"b"
    elif k==5:
        return "aba"+"a"*(b-2)+"b"
    elif k==6:
        return "baa"+"b"*(a-2)+"a"
    else:
        return "b"+"a"*(a-1)+"b"*(b-1)
a,b,k=map(int,input().split())
print(get_num(a,b,k))
