def main():
    n, k = map(int, input().split())
    s = [input() for i in range(n)]
    ans = 0
    for bit in range(1 << 26):
        cnt = 0
        for i in range(n):
            flag = True
            for j in range(len(s[i])):
                if bit & (1 << (ord(s[i][j]) - ord('a'))) == 0:
                    flag = False
                    break
            if flag:
                cnt += 1
        if cnt >= k:
            ans = max(ans, bin(bit).count('1'))
    print(ans)
