def solve():
    S = input()
    red = S.count('0')
    blue = len(S) - red
    print(min(red, blue) * 2)

if __name__ == '__main__':
    solve()