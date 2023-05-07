def main():
    N = int(input())
    A = list(map(int, input().split()))
    count = [0] * (N+1)
    for i in range(N-1):
        count[A[i]] += 1
    for i in range(1, N+1):
        print(count[i])

if __name__ == '__main__':
    main()