def main():
    n = int(input())
    print("Yes" if n % sum(map(int, str(n))) == 0 else "No")

if __name__ == '__main__':
    main()