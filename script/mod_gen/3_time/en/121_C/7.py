def main():
    N, M = map(int, input().split())
    stores = []
    for i in range(N):
        A, B = map(int, input().split())
        stores.append([A, B])
    stores.sort(key=lambda x: x[0])
    ans = 0
    for A, B in stores:
        if M - B >= 0:
            ans += A * B
            M -= B
        else:
            ans += A * M
            break
    print(ans)

if __name__ == '__main__':
    main()