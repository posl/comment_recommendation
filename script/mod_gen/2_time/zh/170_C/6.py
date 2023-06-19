def main():
    x, n = map(int, input().split())
    if n == 0:
        print(x)
        return
    p = [int(i) for i in input().split()]
    for i in range(0, 100):
        if x - i not in p:
            print(x - i)
            return
        if x + i not in p:
            print(x + i)
            return

if __name__ == '__main__':
    main()