def solve():
    s = input()
    if 65 <= ord(s[0]) <= 90 and 65 <= ord(s[-1]) <= 90 and len(s) == 8:
        if 100000 <= int(s[1:-1]) <= 999999:
            print("Yes")
            return
    print("No")
solve()
