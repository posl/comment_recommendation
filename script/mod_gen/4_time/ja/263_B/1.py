def main():
    n = int(input())
    p = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        if p[i] == n:
            ans += 1
        else:
            ans = 1
            j = i
            while p[j] != n:
                j = p[j] - 1
                ans += 1
            break
    print(ans)

if __name__ == '__main__':
    main()