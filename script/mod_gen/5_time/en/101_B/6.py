def main():
    n = int(input())
    s = sum(map(int, str(n)))
    if n % s == 0:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()