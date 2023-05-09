def solve():
    a,s=map(int,input().split())
    if a==s:
        print("Yes")
        return
    if a>s:
        print("No")
        return
    if a==0:
        print("No")
        return
    if (s-a)&1==1:
        print("No")
        return
    print("Yes")
    return
