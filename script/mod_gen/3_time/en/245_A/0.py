def main():
    a, b, c, d = map(int, input().split())
    if a * 60 + b < c * 60 + d:
        print("Takahashi")
    else:
        print("Aoki")
main()

if __name__ == '__main__':
    main()