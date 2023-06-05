def solve():
    s = input()
    t = input()
    for i in range(len(s)):
        if s[i] != t[i]:
            print(i+1)
            break

if __name__ == '__main__':
    solve()