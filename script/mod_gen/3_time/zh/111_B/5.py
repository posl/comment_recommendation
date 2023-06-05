def main():
    n = int(input())
    while True:
        if n%111 == 0:
            print(n)
            break
        n += 1

if __name__ == '__main__':
    main()