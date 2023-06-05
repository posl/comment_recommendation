def solve():
    N = input()
    if len(N) == 2:
        print(int(N[0]) * int(N[1]))
        return
    if len(N) == 3:
        print(int(N[0]) * int(N[1:]))
        return
    if len(N) == 4:
        print(9 * int(N[0]) * int(N[1:]))
        return
    if len(N) == 5:
        print(9 * int(N[0]) * int(N[1:]))
        return
    if len(N) == 6:
        print(9 * int(N[0]) * int(N[1:]))
        return
    if len(N) == 7:
        print(9 * int(N[0]) * int(N[1:]))
        return
    if len(N) == 8:
        print(9 * int(N[0]) * int(N[1:]))
        return
    if len(N) == 9:
        print(9 * int(N[0]) * int(N[1:]))
        return
    if len(N) == 10:
        print(9 * int(N[0]) * int(N[1:]))
        return

if __name__ == '__main__':
    solve()