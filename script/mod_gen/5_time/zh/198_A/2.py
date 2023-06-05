def main():
    N = int(input())
    if N%2 == 0:
        print(int(N/2-1))
    else:
        print(0)

if __name__ == '__main__':
    main()