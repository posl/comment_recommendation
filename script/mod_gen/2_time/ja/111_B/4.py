def main():
    N = int(input())
    while True:
        if N % 111 == 0:
            print(N)
            break
        N += 1

if __name__ == '__main__':
    main()