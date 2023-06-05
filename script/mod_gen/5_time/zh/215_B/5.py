def main():
    N = int(input())
    k = 0
    while N >= 2:
        N = N/2
        k = k + 1
    print(k)

if __name__ == '__main__':
    main()