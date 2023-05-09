def main():
    N = int(input())
    if -2**31 <= N < 2**31:
        print("Yes")
    else:
        print("No")
main()

if __name__ == '__main__':
    main()