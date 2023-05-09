def solve():
    A, B, C, D, E, F, X = map(int, input().split())
    takahashi = (A + C) * B
    aoki = D * E
    if takahashi > aoki:
        print("Takahashi")
    elif takahashi < aoki:
        print("Aoki")
    else:
        print("Draw")
solve()

if __name__ == '__main__':
    solve()