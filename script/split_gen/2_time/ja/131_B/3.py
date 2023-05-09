def main():
    N, L = map(int, input().split())
    ans = 0
    for i in range(1, N):
        ans += L + i - 1
    if L <= 0 and L + N - 1 >= 0:
        print(ans)
    elif L > 0:
        print(ans - L)
    else:
        print(ans - (L + N - 1))
