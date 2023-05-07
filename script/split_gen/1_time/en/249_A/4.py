def main():
    A, B, C, D, E, F, X = map(int, input().split())
    taka = (A + C) * B
    aoki = (D + F) * E
    if taka > aoki:
        print("Takahashi")
    elif taka < aoki:
        print("Aoki")
    else:
        print("Draw")
