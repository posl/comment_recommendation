def main():
    N = int(input())
    d = {}
    for i in range(N):
        L = list(map(int, input().split(" ")))
        L = L[1:]
        L = tuple(L)
        if L not in d:
            d[L] = 1
        else:
            d[L] += 1
    print(len(d))

if __name__ == '__main__':
    main()