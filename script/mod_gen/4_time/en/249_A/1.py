def main():
    a, b, c, d, e, f, x = map(int, input().split())
    takahashi = (a + c) * b
    aoki = d * e
    if takahashi > aoki:
        print("Takahashi")
    elif aoki > takahashi:
        print("Aoki")
    else:
        print("Draw")
main()

if __name__ == '__main__':
    main()