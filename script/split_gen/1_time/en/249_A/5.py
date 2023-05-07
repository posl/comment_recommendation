def main():
    a, b, c, d, e, f, x = map(int, input().split())
    takahashi = 0
    aoki = 0
    takahashi = (a + c) * b
    aoki = d * e
    if takahashi == aoki:
        print("Draw")
    elif takahashi > aoki:
        print("Takahashi")
    elif takahashi < aoki:
        print("Aoki")
main()
