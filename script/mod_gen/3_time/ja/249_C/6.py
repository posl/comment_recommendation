def main():
    n,k = map(int, input().split())
    s = [input() for _ in range(n)]
    alp = [0 for _ in range(26)]
    for i in range(n):
        for j in range(len(s[i])):
            alp[ord(s[i][j])-97] += 1
    alp.sort()
    ans = 0
    for i in range(26):
        if alp[25-i] >= k:
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()