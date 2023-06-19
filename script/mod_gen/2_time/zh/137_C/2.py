def main():
    N = int(input())
    s = []
    for i in range(N):
        s.append(input())
    s.sort()
    s.append("")
    count = 0
    ans = 0
    for i in range(N):
        if s[i] == s[i + 1]:
            count += 1
        else:
            ans += count * (count + 1) // 2
            count = 0
    print(ans)

if __name__ == '__main__':
    main()