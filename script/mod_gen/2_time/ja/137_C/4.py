def main():
    N = int(input())
    s = [input() for _ in range(N)]
    s.sort()
    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            if s[i] == s[j]:
                continue
            if "".join(sorted(s[i])) == "".join(sorted(s[j])):
                ans += 1
    print(ans)

if __name__ == '__main__':
    main()