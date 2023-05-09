def main():
    # input
    A, B, C, D, E, F, X = map(int, input().split())
    # compute
    takahashi = (A + C) * B
    aoki = D * E
    if takahashi > aoki:
        winner = 'Takahashi'
    elif takahashi < aoki:
        winner = 'Aoki'
    else:
        winner = 'Draw'
    # output
    print(winner)
