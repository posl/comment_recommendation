def main():
    n = int(input())
    for i in range(1, 10**6):
        if i*i > n:
            print((i-1)*2)
            break

if __name__ == '__main__':
    main()