def solve():
    A, B, C, D, E, F, X = map(int, input().split())
    T = 0
    Taka = 0
    Aoki = 0
    while True:
        if T % (C + B) < C:
            Taka += A
        if T % (F + E) < F:
            Aoki += D
        T += 1
        if Taka + A > X and Aoki + D > X:
            print("Draw")
            break
        elif Taka + A > X:
            print("Aoki")
            break
        elif Aoki + D > X:
            print("Takahashi")
            break

if __name__ == '__main__':
    solve()