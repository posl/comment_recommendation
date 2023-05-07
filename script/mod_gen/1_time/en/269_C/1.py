def main():
    N = int(input())
    x = 0
    while x <= N:
        if x & N == x:
            print(x)
        x += 1

if __name__ == '__main__':
    main()