def main():
    N = input()
    if N == N[::-1]:
        print("Yes")
    else:
        print("No")
    return

if __name__ == '__main__':
    main()