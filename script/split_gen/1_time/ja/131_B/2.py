def main():
    N, L = map(int, input().split())
    sum = 0
    for i in range(1, N+1):
        sum += L + i - 1
    if L >= 0:
        print(sum - L - 1)
    elif L + N - 1 < 0:
        print(sum - L - N)
    else:
        print(sum)
