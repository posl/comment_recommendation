def main():
    N, K = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    b = [0] * N
    for i in range(N):
        b[i] = a[i] - 1
    ans = [0] * N
    for i in range(N):
        ans[i] = K // N
    for i in range(K % N):
        ans[i] += 1
    for i in range(N):
        print(ans[b[i]])

if __name__ == '__main__':
    main()