def main():
    a, b, c, d = map(int, input().split())
    if a > c:
        print("Aoki")
    elif a == c:
        if b >= d:
            print("Takahashi")
        else:
            print("Aoki")
    else:
        print("Takahashi")

if __name__ == '__main__':
    main()