def main():
    N, L = map(int, input().split())
    ans = 0
    if L >= 0:
        ans = (L + N - 1) * (L + N) // 2 - L
    elif L + N - 1 < 0:
        ans = (L + N - 1) * (L + N) // 2 - L
    else:
        ans = (L + N - 1) * (L + N) // 2
    print(ans)
