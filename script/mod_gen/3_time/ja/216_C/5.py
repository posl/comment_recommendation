def solve():
    N = int(input())
    S = ""
    while N > 0:
        if N % 2 == 0:
            S = "B" + S
            N //= 2
        else:
            S = "A" + S
            N -= 1
    print(S)
    return 0

if __name__ == '__main__':
    solve()