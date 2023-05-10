def main():
    n, k, a = map(int, input().split())
    if k % n == 0:
        print(0)
    else:
        print(1)

if __name__ == '__main__':
    main()