def solve():
    a,b,w=map(int,input().split())
    w*=1000
    ans_min=0
    ans_max=0
    for i in range(1,1000000):
        if a*i<=w and w<=b*i:
            ans_min=i
            break
    for i in range(1,1000000):
        if a*i>w or w>b*i:
            ans_max=i-1
            break
    if ans_min==0 and ans_max==0:
        print("UNSATISFIABLE")
    else:
        print(ans_min,ans_max)

if __name__ == '__main__':
    solve()