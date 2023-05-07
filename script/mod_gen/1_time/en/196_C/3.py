def main():
    N = int(input())
    ans = 0
    for i in range(1, N + 1):
        if len(str(i)) % 2 == 0:
            s = str(i)
            if s[:len(s) // 2] == s[len(s) // 2:]:
                ans += 1
    print(ans)

if __name__ == '__main__':
    main()