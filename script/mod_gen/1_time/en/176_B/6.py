def main():
    N = input()
    if N == "0":
        print("Yes")
        return
    if int(N[-1]) % 2 == 0:
        print("No")
        return
    if sum(map(int, N)) % 9 == 0:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()