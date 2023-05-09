def main():
    n = int(input())
    s = [input() for _ in range(n)]
    ans = 0
    for i in range(10):
        cnt = 0
        for j in range(n):
            if s[j][i] == str(i):
                cnt += 1
        if cnt == 0:
            continue
        ans += 10 - cnt
    print(ans)

if __name__ == '__main__':
    main()