def solve():
    # 编写从这里开始
    s = input()
    if s[0] == s[1] == s[2]:
        print(-1)
    elif s[0] == s[1]:
        print(s[2])
    elif s[0] == s[2]:
        print(s[1])
    elif s[1] == s[2]:
        print(s[0])
    else:
        print(s[0])

if __name__ == '__main__':
    solve()