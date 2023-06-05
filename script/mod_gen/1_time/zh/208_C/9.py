def main():
    N, K = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    a.append(a[0] + K)
    b = [0] * N
    for i in range(N):
        b[i] = a[i + 1] - a[i]
    m = min(b)
    min_index = b.index(m)
    for i in range(N):
        if i == min_index:
            print(a[i] + K // N + 1)
        else:
            print(a[i] + K // N)

if __name__ == '__main__':
    main()