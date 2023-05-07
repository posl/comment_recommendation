def main():
    a, b = map(int, input().split())
    if a + b == 16:
        print("Yay!")
    else:
        print(":(")

if __name__ == '__main__':
    main()