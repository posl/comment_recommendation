def main():
    a, b = map(int, input().split())
    if a + b <= 15 and a <= 8 and b <= 8:
        print("Yay!")
    else:
        print(":(")

if __name__ == '__main__':
    main()