def main():
    x, n = map(int, input().split())
    p = list(map(int, input().split()))
    if n == 0:
        print(x)
        return
    if x not in p:
        print(x)
        return
    for i in range(100):
        if x - i not in p:
            print(x - i)
            return
        if x + i not in p:
            print(x + i)
            return

if __name__ == '__main__':
    main()