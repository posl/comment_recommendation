def main():
    N = int(input())
    A = list(map(int, input().split()))
    #print(A)
    ans = 0
    for i in range(N):
        if A[i] != i + 1:
            ans += 1
    if ans == N:
        ans = -1
    print(ans)
