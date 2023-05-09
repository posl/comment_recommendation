def main():
    a,b,c,d = map(int, input().split())
    if a == c:
        if b < d:
            print("Takahashi")
        else:
            print("Aoki")
    elif a < c:
        print("Takahashi")
    else:
        print("Aoki")

if __name__ == '__main__':
    main()