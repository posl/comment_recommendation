def f():
    N = int(input())
    X,Y = map(int,input().split())
    A = []
    B = []
    for i in range(N):
        a,b = map(int,input().split())
        A.append(a)
        B.append(b)
    ans = float('inf')
    for i in range(N):
        for j in range(N):
            if A[i]+B[j]>=X and A[i]+B[j]>=Y:
                ans = min(ans,i+j+2)
    if ans == float('inf'):
        print(-1)
    else:
        print(ans)

if __name__ == '__main__':
    f()