def main():
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    ans = []
    for i in range(n):
        if a[i] != x:
            ans.append(a[i])
    for i in range(len(ans)):
        print(ans[i], end=" ")
    print()

if __name__ == '__main__':
    main()