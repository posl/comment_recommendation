def solve():
    s = input()
    t = input()
    print(sum([1 for i in range(len(s)) if s[i] != t[i]]))
solve()

if __name__ == '__main__':
    solve()