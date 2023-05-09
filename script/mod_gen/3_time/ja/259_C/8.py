def solve():
    S = input()
    T = input()
    if S == T:
        print("Yes")
        return
    s = S
    for i in range(len(S)):
        if s == T:
            print("Yes")
            return
        s = s[:i] + s[i] + s[i:]
    print("No")

if __name__ == '__main__':
    solve()