def main():
    n = int(input())
    print(n, n)
    for i in range(n-1):
        print(i+1, i+2, 0)
    for i in range(n-1):
        print(i+1, i+2, 1)

if __name__ == '__main__':
    main()