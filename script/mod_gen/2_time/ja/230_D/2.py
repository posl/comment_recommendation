def main():
    N,D = map(int,input().split())
    L = []
    R = []
    for i in range(N):
        l,r = map(int,input().split())
        L.append(l)
        R.append(r)
    ans = 0
    for i in range(N):
        ans += (R[i] - L[i] + 1)
    ans = ans / D
    print(int(ans))

if __name__ == '__main__':
    main()