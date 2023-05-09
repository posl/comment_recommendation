def main():
    N = int(input())
    if N % 111 == 0:
        print(N)
    else:
        print(N + (111 - N % 111))

if __name__ == '__main__':
    main()