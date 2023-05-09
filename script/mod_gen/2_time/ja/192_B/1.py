def solve():
    s = input()
    if s[0::2].islower() and s[1::2].isupper():
        print("Yes")
    else:
        print("No")
solve()

if __name__ == '__main__':
    solve()