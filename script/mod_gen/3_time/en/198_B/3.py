def main():
    N = input()
    N = N[::-1]
    if N == N[::-1]:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()