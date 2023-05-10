def main():
    N, M = map(int, input().split())
    L = []
    R = []
    for i in range(M):
        l, r = map(int, input().split())
        L.append(l)
        R.append(r)
    L = max(L)
    R = min(R)
    if L <= R:
        print(R - L + 1)
    else:
        print(0)

if __name__ == '__main__':
    main()