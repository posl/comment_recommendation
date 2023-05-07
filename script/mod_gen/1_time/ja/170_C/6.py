def main():
    x = int(input().split()[0])
    p = set(map(int, input().split()))
    for i in range(1000):
        if x - i not in p:
            print(x - i)
            return
        if x + i not in p:
            print(x + i)
            return

if __name__ == '__main__':
    main()