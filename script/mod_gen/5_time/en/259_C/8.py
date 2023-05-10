def solve():
    s = input()
    t = input()
    while True:
        if s == t:
            print("Yes")
            break
        if len(s) >= len(t):
            print("No")
            break
        if t[-1] == "A":
            t = t[:-1]
        else:
            t = t[:-1][::-1]

if __name__ == '__main__':
    solve()