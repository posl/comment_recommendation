def main():
    N, L = map(int, input().split())
    apple = [L + i - 1 for i in range(1, N + 1)]
    apple.sort()
    if L >= 0:
        print(sum(apple) - apple[0])
    elif L + N - 1 <= 0:
        print(sum(apple) - apple[-1])
    else:
        print(sum(apple))
main()
