def main():
    N = int(input())
    S = sum(map(int, str(N)))
    if N % S == 0:
        print("Yes")
    else:
        print("No")
main()

if __name__ == '__main__':
    main()