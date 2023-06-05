def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    a.append(0)
    ans = [0] * n
    cnt = 1
    for i in range(n):
        if a[i] != a[i + 1]:
            for j in range(cnt, i + 1):
                ans[j] = cnt - 1
            cnt = i + 2
    print(*ans, sep='\n')

if __name__ == '__main__':
    main()