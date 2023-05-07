def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        if A[i] == i + 1:
            if i + 1 < N and A[i + 1] == i + 2:
                ans += 1
            else:
                ans += 1
                break
    print(ans)
