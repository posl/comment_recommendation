def main():
    N = int(input())
    a = list(map(int, input().split()))
    a = [i - 1 for i in a]
    b = [0] * N
    for i in range(N):
        b[a[i]] += 1
    for i in range(N):
        if b[i] > i + 1:
            print(-1)
            return
    print(N - sum(b))

if __name__ == '__main__':
    main()