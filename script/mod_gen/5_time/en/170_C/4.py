def main():
    x, n = map(int, input().split())
    if n == 0:
        print(x)
        exit()
    p = sorted(map(int, input().split()))
    for i in range(100):
        if x - i not in p:
            print(x - i)
            exit()
        if x + i not in p:
            print(x + i)
            exit()

if __name__ == '__main__':
    main()