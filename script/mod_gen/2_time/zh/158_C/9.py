def main():
    a, b = map(int, input().split())
    for i in range(1, 1000):
        if a == int(i * 0.08) and b == int(i * 0.1):
            print(i)
            exit()
    print(-1)

if __name__ == '__main__':
    main()