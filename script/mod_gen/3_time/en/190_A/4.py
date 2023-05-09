def main():
    a, b, c = map(int, input().split())
    if a > b:
        print("Takahashi")
    elif a == b:
        if c == 0:
            print("Aoki")
        else:
            print("Takahashi")
    else:
        print("Aoki")

if __name__ == '__main__':
    main()