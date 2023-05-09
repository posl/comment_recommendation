def main():
    H, W, N = map(int, input().split())
    x = []
    y = []
    for _ in range(N):
        a, b = map(int, input().split())
        x.append(a)
        y.append(b)
    x = list(set(x))
    y = list(set(y))
    x.sort()
    y.sort()
    for i in range(N):
        a, b = map(int, input().split())
        print(x.index(a) + 1, y.index(b) + 1)

if __name__ == '__main__':
    main()