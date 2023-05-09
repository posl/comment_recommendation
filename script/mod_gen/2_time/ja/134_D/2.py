def main():
    N = int(input())
    a = list(map(int, input().split()))
    if a[0] == 1:
        print(-1)
        return
    if N == 1:
        print(0)
        return
    if a[1] == 1:
        print(-1)
        return
    if N == 2:
        print(0)
        return
    if a[2] == 1:
        print(-1)
        return
    if N == 3:
        print(0)
        return
    #3以上
    for i in range(3, N):
        if a[i] == 1:
            if a[i-1] == 0 and a[i-2] == 0 and a[i-3] == 0:
                print(-1)
                return
    #print(a)
    ans = []
    for i in range(N):
        if a[i] == 1:
            ans.append(i+1)
    print(len(ans))
    print(*ans)

if __name__ == '__main__':
    main()