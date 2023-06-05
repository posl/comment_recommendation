def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.append(a[0])
    a.append(a[1])
    ans = 0
    for i in range(n):
        ans += max(a[i], a[i+1])
    print(ans)

if __name__ == '__main__':
    main()