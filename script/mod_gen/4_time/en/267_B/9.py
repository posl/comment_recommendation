def solve():
    print("Yes" if input()[0] == "0" and input().count("1") >= 2 else "No")
solve()

if __name__ == '__main__':
    solve()