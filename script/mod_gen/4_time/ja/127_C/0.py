def main():
    N, M = map(int, input().split())
    L = []
    R = []
    for i in range(M):
        l, r = map(int, input().split())
        L.append(l)
        R.append(r)
    print(max(0, min(R) - max(L) + 1))

if __name__ == '__main__':
    main()