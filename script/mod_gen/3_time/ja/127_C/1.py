def main():
    N, M = map(int, input().split())
    L = []
    R = []
    for i in range(M):
        l, r = map(int, input().split())
        L.append(l)
        R.append(r)
    L.sort()
    R.sort()
    if L[-1] <= R[0]:
        print(R[0] - L[-1] + 1)
    else:
        print(0)

if __name__ == '__main__':
    main()