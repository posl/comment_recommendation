def main():
    N = int(input())
    ans = 0
    for A in range(1, N+1):
        for B in range(A, N//A+1):
            ans += min(N//A//B, N//A - B + 1)
    print(ans)
