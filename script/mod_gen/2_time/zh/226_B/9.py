def main():
    n = int(input())
    a = []
    for i in range(n):
        a.append(list(map(int, input().split()))[1:])
    a.sort()
    ans = 1
    for i in range(n-1):
        if a[i] != a[i+1]:
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()