def solve():
    N = int(input())
    ans = N * 1.08
    if ans < 206:
        print("Yay!")
    elif ans == 206:
        print("so-so")
    else:
        print(":(")
solve()

if __name__ == '__main__':
    solve()