def main():
    x, n = map(int, input().split())
    p = list(map(int, input().split()))
    p = set(p)
    for i in range(100):
        if x - i not in p:
            print(x - i)
            break
        if x + i not in p:
            print(x + i)
            break

if __name__ == '__main__':
    main()