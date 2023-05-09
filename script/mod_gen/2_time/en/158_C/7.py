def main():
    A, B = map(int, input().split())
    for i in range(1, 1000):
        if A == i // 0.08 and B == i // 0.1:
            print(i)
            return
    print(-1)
    return

if __name__ == '__main__':
    main()