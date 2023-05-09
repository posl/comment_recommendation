def main():
    a, b, c = map(int, input().split())
    print("Takahashi" if a > b or (a == b and c == 0) else "Aoki")

if __name__ == '__main__':
    main()