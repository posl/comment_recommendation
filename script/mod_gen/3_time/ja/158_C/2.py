def main():
    A, B = map(int, input().split())
    for i in range(1, 1000):
        if i * 8 // 100 == A and i * 10 // 100 == B:
            print(i)
            return
    print(-1)
    return

if __name__ == '__main__':
    main()