def main():
    N, D = map(int, input().split())
    cnt = 0
    for i in range(N):
        X, Y = map(int, input().split())
        if (X**2 + Y**2)**(1/2) <= D:
            cnt += 1
    print(cnt)

if __name__ == '__main__':
    main()