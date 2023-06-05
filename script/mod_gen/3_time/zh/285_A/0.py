def main():
    a, b = map(int, input().split())
    if a < b and a >= 1 and b <= 15:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()