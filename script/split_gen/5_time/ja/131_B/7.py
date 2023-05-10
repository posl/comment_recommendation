def main():
    N, L = map(int, input().split())
    if L >= 0:
        print((L + N - 1) * (L + N) // 2 - L)
    elif L < 0 and L + N - 1 >= 0:
        print((L + N - 1) * (L + N) // 2)
    else:
        print((L + N - 1) * (L + N) // 2 - (L + N - 1))
