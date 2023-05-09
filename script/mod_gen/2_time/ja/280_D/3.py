def main():
    N = int(input())
    i = 2
    while True:
        if N % i == 0:
            print(i)
            break
        i += 1

if __name__ == '__main__':
    main()