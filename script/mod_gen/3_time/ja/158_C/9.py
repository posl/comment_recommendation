def main():
    A, B = map(int, input().split())
    for i in range(1, 1000):
        if i * 0.08 - A == 0 and i * 0.1 - B == 0:
            print(i)
            return
    print(-1)

if __name__ == '__main__':
    main()