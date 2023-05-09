def main():
    N, M = map(int, input().split())
    L = []
    R = []
    for _ in range(M):
        l, r = map(int, input().split())
        L.append(l)
        R.append(r)
    L = max(L)
    R = min(R)
    print(max(0, R - L + 1))

if __name__ == '__main__':
    main()