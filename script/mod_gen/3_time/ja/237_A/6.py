def main():
    n = int(input())
    print("Yes") if n >= -2**31 and n < 2**31 else print("No")

if __name__ == '__main__':
    main()