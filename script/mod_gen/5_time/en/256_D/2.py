def main():
    N = int(input())
    L = []
    R = []
    for i in range(N):
        l, r = map(int, input().split())
        L.append(l)
        R.append(r)
    L = sorted(L)
    R = sorted(R)
    print(L, R)
    print(R[0] - L[-1] + 1)

if __name__ == '__main__':
    main()