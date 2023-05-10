def main():
    X, Y, N = map(int, input().split())
    cnt = 0
    for i in range(1, N+1):
        if i % 3 == 0:
            cnt += Y
        else:
            cnt += X
    print(cnt)
main()

if __name__ == '__main__':
    main()