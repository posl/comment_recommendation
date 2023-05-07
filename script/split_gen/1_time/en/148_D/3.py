def main():
    N = int(input())
    A = list(map(int, input().split()))
    if A[0] != 1:
        print(-1)
    else:
        ans = 0
        for i in range(N-1):
            if A[i+1] - A[i] > 1:
                print(-1)
                return
            elif A[i+1] == A[i] + 1:
                ans += 1
            else:
                ans += A[i+1]
        print(ans)
