def main():
    n = int(input())
    a = [int(x) for x in input().split()]
    if a[0] == 1:
        print(-1)
        return
    if n == 1:
        print(0)
        return
    if a[1] == 1:
        print(-1)
        return
    if n == 2:
        print(0)
        return
    if a[2] == 1:
        print(-1)
        return
    ans = []
    for i in range(3, n):
        if a[i] == 1:
            ans.append(i+1)
    print(len(ans))
    print(' '.join(map(str, ans)))

if __name__ == '__main__':
    main()