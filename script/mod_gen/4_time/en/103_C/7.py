def main():
    N = int(input())
    a = list(map(int, input().split()))
    a.sort()
    max = 0
    for i in range(N):
        max += a[i] * (N-i-1)
    print(max)

if __name__ == '__main__':
    main()