def main():
    N = int(input())
    A = list(map(int, input().split()))
    count = [0] * N
    for a in A:
        count[a - 1] += 1
    ans = 0
    for i in range(N):
        ans += count[i] * (count[i] - 1) // 2
    for i in range(N):
        print(ans - (count[A[i] - 1] - 1))

if __name__ == '__main__':
    main()