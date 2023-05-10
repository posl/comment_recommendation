def main():
    x,k = map(int, input().split())
    for i in range(k):
        if x % 10 == 0:
            x = x // 10
        else:
            x += 10 - (x % 10)
    print(x)

if __name__ == '__main__':
    main()