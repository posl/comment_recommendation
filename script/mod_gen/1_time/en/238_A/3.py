def main():
    n = int(input())
    if 2**n > n**2:
        print("Yes")
    else:
        print("No")
    return 0

if __name__ == '__main__':
    main()