def main():
    n = int(input())
    p = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        cnt = 0
        j = i
        while j != -1:
            j = p[j] - 1
            cnt += 1
        ans = max(ans, cnt)
    print(ans)

if __name__ == '__main__':
    main()