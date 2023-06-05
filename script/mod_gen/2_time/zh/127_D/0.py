def main():
    n, m = map(int, input().split())
    L = []
    R = []
    for i in range(m):
        l, r = map(int, input().split())
        L.append(l)
        R.append(r)
    L.sort()
    R.sort()
    if L[m-1] > R[0]:
        print(0)
    else:
        print(R[0]-L[m-1]+1)

if __name__ == '__main__':
    main()