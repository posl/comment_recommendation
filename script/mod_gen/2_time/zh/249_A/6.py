def main():
    a, b, c, d, e, f, x = map(int, input().split())
    takahashi = 0
    aoki = 0
    takahashi = a * b * x
    for i in range(x):
        if i % (c + d) < c:
            aoki += e
    if takahashi > aoki:
        print("Takahashi")
    elif takahashi < aoki:
        print("Aoki")
    else:
        print("Draw")

if __name__ == '__main__':
    main()