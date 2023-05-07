def main():
    a, b, c, d = map(int, input().split())
    if a == c and b == d:
        print("Takahashi")
    elif a == c and b > d:
        print("Takahashi")
    elif a == c and b < d:
        print("Aoki")
    elif a > c:
        print("Takahashi")
    elif a < c:
        print("Aoki")

if __name__ == '__main__':
    main()