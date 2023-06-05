def solve():
    n,x = map(int,input().split())
    a = list(map(int,input().split()))
    a = [i for i in a if i%2==0]
    if x>=sum(a):
        print("Yes")
    else:
        print("No")
solve()
