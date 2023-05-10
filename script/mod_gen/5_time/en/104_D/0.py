def main():
    s = input()
    s = s.replace('?', '0')
    s = s.replace('A', '1')
    s = s.replace('B', '2')
    s = s.replace('C', '3')
    s = s.replace('0', 'ABC')
    s = s.replace('1', 'AB')
    s = s.replace('2', 'BC')
    s = s.replace('3', 'AC')
    s = list(s)
    s = list(map(int, s))
    MOD = 10**9 + 7
    ans = 0
    cnt = 0
    for i in range(len(s)):
        if s[i] == 1 or s[i] == 2 or s[i] == 3:
            cnt += 1
        elif s[i] == 0:
            ans += cnt
        else:
            ans += cnt
            cnt = 0
    print(ans % MOD)
main()

if __name__ == '__main__':
    main()