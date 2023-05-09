def main():
    n = int(input())
    p = list(map(int, input().split()))
    p = [0] + p
    ans = 0
    for i in range(1, n + 1):
        cnt = 0
        j = i
        while j != 0:
            j = p[j]
            cnt += 1
        ans = max(ans, cnt)
    print(ans)
main()

if __name__ == '__main__':
    main()