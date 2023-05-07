def main():
    N = int(input())
    A = list(map(int, input().split()))
    max = 0
    now = 0
    for i in range(N):
        now += A[i]
        if now > max:
            max = now
    print(max)

if __name__ == '__main__':
    main()