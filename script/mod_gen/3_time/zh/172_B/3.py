def solve():
    s = input()
    t = input()
    if s == t:
        print(0)
        return
    i = 0
    while i < len(s) and i < len(t):
        if s[i] != t[i]:
            break
        i += 1
    print(len(s) - i + len(t) - i)

if __name__ == '__main__':
    solve()