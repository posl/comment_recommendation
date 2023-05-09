def main():
    N, L = map(int, input().split())
    apple = [L + i - 1 for i in range(1, N + 1)]
    apple.sort()
    print(sum(apple) - apple[0])
main()
