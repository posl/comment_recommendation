def main():
    a,b,c,d = map(int, input().split())
    if a > c:
        print("Takahashi")
    elif a < c:
        print("Aoki")
    elif b > d:
        print("Takahashi")
    elif b < d:
        print("Aoki")
    else:
        print("Same")

if __name__ == '__main__':
    main()