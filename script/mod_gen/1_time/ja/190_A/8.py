def main():
    a,b,c = map(int, input().split())
    if a > b:
        print("Takahashi")
    elif a < b:
        print("Aoki")
    elif c == 0:
        print("Aoki")
    elif c == 1:
        print("Takahashi")

if __name__ == '__main__':
    main()