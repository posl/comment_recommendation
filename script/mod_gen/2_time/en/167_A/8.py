def solve():
    s = input()
    t = input()
    if t == s + t[-1]:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    solve()