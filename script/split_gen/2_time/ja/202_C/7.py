def main():
    N = int(input())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    C = list(map(int,input().split()))
    ans = 0
    for i in range(N):
        ans += B.count(C[A[i]-1])
    print(ans)
