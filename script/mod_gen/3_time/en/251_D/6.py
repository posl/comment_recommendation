def main():
    w = int(input())
    n = w // 2
    print(n)
    print(' '.join([str(i) for i in range(1, n+1)]))

if __name__ == '__main__':
    main()