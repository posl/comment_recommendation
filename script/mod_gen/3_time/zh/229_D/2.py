def main():
    s = input()
    k = int(input())
    s = list(s)
    s.append('X')
    s.insert(0, 'X')
    s.append('X')
    s.insert(0, 'X')
    ans = 0
    for i in range(1, len(s)):
        if s[i] == '.':
            ans += 1
        else:
            ans = 0
        if ans > k:
            print(k)
            exit(0)
    print(ans)

if __name__ == '__main__':
    main()