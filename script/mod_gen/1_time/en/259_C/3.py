def solve():
    s = input()
    t = input()
    if len(s) > len(t):
        print("No")
        return
    i, j = 0, 0
    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            i += 1
        j += 1
    if i == len(s):
        print("Yes")
    else:
        print("No")
solve()

if __name__ == '__main__':
    solve()