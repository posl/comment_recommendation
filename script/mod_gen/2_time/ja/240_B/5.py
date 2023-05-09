def main():
    N = int(input())
    a = list(map(int, input().split()))
    a.sort()
    a.append(0)
    ans = 0
    for i in range(N):
        if a[i] != a[i+1]:
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()