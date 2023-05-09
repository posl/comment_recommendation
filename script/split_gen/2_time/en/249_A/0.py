def main():
    a, b, c, d, e, f, x = map(int, input().split())
    takahashi = (a + c) * b
    aoki = d * e
    if takahashi > aoki:
        print("Takahashi")
    elif takahashi < aoki:
        print("Aoki")
    else:
        print("Draw")
