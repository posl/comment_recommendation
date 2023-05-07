def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    A = [0] + A
    count = [0] * (A[-1] + 1)
    for i in range(1, N + 1):
        count[A[i]] += 1
    for i in range(2, A[-1] + 1):
        for j in range(2, A[-1] // i + 1):
            count[i] += count[i * j]
    ans = 0
    for i in range(1, N + 1):
        if count[A[i]] == 1:
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()