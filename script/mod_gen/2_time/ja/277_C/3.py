def main():
    N = int(input())
    a = [0] * N
    b = [0] * N
    for i in range(N):
        a[i], b[i] = map(int, input().split())
    a.sort()
    b.sort()
    if N % 2 == 0:
        ans = b[N // 2] - a[N // 2 - 1] + 1
    else:
        ans = b[N // 2] - a[N // 2] + 1
    print(ans)

if __name__ == '__main__':
    main()