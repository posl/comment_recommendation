def main():
    A, B = map(int, input().split())
    for i in range(1, 1001):
        if i * 0.08 // 1 == A and i * 0.1 // 1 == B:
            print(i)
            return
    print(-1)

if __name__ == '__main__':
    main()