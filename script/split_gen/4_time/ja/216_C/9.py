def solve():
    n=int(input())
    res=[]
    while n>0:
        if n%2==0:
            n//=2
            res.append('B')
        else:
            n-=1
            res.append('A')
    print(''.join(reversed(res)))
solve()
