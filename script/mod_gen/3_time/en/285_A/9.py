def main():
    a, b = map(int, input().split())
    if a < b and b - a == 1:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()