def main():
    a, b, c, d = map(int, input().split())
    if a > c:
        print("Takahashi")
    elif a < c:
        print("Aoki")
    elif a == c:
        if b > d:
            print("Takahashi")
        elif b < d:

if __name__ == '__main__':
    main()