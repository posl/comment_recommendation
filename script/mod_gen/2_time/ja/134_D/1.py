def main():
    N = int(input())
    a = list(map(int, input().split()))
    if a[0] == 1:
        print(-1)
        return
    if N == 1:
        print(0)
        return
    if N == 2:
        if a[1] == 1:
            print(-1)
        else:
            print(0)
        return
    ans = []
    for i in range(1, N):
        if a[i] == 1:
            ans.append(i)
            ans.append(i)
            ans.append(i - 1)
    print(len(ans))
    for i in ans:
        print(i, end=" ")
    print()

if __name__ == '__main__':
    main()