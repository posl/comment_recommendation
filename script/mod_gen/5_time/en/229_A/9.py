def solve():
    s1 = input()
    s2 = input()
    print("Yes" if s1.count("#") >= 2 or s2.count("#") >= 2 else "No")

if __name__ == '__main__':
    solve()