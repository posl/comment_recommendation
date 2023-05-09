def main():
    N = int(input())
    if N % 2 == 0:
        print(N/2/N)
    else:
        print((N+1)/2/N)

if __name__ == '__main__':
    main()