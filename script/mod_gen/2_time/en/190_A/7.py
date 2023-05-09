def main():
    a, b, c = map(int, input().split())
    if a == b:
        print("Aoki" if c else "Takahashi")
    else:
        print("Takahashi" if a > b else "Aoki")

if __name__ == '__main__':
    main()