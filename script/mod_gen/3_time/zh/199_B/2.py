def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    x = 0
    for i in range(N):
        x = max(x, A[i])
    y = 1000
    for i in range(N):
        y = min(y, B[i])
    print(max(0, y - x + 1))

if __name__ == '__main__':
    main()