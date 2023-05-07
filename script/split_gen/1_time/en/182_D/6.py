def main():
    N = int(input())
    A = list(map(int, input().split()))
    #print(N)
    #print(A)
    ans = 0
    for i in range(N):
        ans += A[i]
        if ans < 0:
            ans = 0
    print(ans)
