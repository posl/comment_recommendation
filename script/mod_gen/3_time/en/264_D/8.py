def main():
    s = input()
    goal = "atcoder"
    ans = 0
    for i in range(7):
        if s[i] != goal[i]:
            for j in range(7, i, -1):
                if s[j] == goal[i]:
                    ans += j - i
                    s = s[:i] + s[j] + s[i + 1:j] + s[i] + s[j + 1:]
                    break
    print(ans)
main()

if __name__ == '__main__':
    main()