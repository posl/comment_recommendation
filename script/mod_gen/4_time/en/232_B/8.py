def solve():
    s = input()
    t = input()
    s = s + s
    if t in s:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    solve()