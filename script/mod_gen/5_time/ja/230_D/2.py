def main():
    N, D = map(int, input().split())
    L = []
    R = []
    for i in range(N):
        l, r = map(int, input().split())
        L.append(l)
        R.append(r)
    L.sort()
    R.sort()
    ans = 0
    count = 0
    for i in range(N):
        if L[i] - R[i] > 0:
            count += 1
        else:
            count -= 1
        if count > ans:
            ans = count
    print(ans)

if __name__ == '__main__':
    main()