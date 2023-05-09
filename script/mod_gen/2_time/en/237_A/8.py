def main():
    N = int(input())
    if N >= (-2**31) and N < (2**31):
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()