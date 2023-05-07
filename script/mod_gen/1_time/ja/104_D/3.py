def main():
    S = input()
    Q = S.count('?')
    MOD = 10**9 + 7
    ans = 0
    for i in range(3**Q):
        T = ''
        j = i
        for c in S:
            if c == '?':
                T += chr(ord('A') + j % 3)
                j //= 3
            else:
                T += c
        cnt = 0
        for k in range(len(T) - 2):
            if T[k] == 'A' and T[k+1] == 'B' and T[k+2] == 'C':
                cnt += 1
        ans += cnt
        ans %= MOD
    print(ans)

if __name__ == '__main__':
    main()