def solve():
    s = input().split()
    t = input().split()
    if s == t:
        print("Yes")
    elif s == t[::-1]:
        print("Yes")
    else:
        print("No")
solve()
