def main():
    N = int(input())
    A = list(map(int,input().split()))
    ans = [0]*(2*N+1)
    for i in range(N):
        ans[A[i]] = i+1
    for i in range(1,N+1):
        x = ans[i]
        print(0)
        print(x)
        print(x)
        print(x+1)
        print(x+1)
        print(x+2)
        print(x+2)
        print(x+1)
        print(x+1)
