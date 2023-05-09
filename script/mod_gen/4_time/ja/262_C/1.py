def main():
    N = int(input())
    a = list(map(int, input().split()))
    b = [0] * N
    for i in range(N):
        b[a[i] - 1] = i + 1
    ans = 0
    for i in range(N):
        if b[i] == i + 1:
            continue
        else:
            ans += 1
            b[a[i] - 1] = b[i]
            a[b[i] - 1] = a[i]
    print(ans)

if __name__ == '__main__':
    main()