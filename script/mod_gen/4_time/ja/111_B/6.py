def main():
    N = int(input())
    while True:
        N += 1
        if N%111 == 0:
            print(N)
            break

if __name__ == '__main__':
    main()