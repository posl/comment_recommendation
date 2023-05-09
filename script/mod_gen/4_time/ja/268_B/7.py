def solve():
    # ===CODE===
    S = input()
    T = input()
    if S == T[:len(S)]:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    solve()