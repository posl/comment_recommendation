def main():
    import sys
    input = sys.stdin.readline
    N = int(input())
    A = list(map(int, input().split()))
    A = [0] + A
    # i = 1, 2, ..., N
    # min(A[i], A[j]) = i
    # max(A[i], A[j]) = j
    # i < j
    # A[i] が i であるものの個数
    count = [0] * (N + 1)
    for i in range(1, N + 1):
        count[A[i]] += 1
    # A[j] が j であるものの個数
    count2 = [0] * (N + 1)
    for j in range(1, N + 1):
        count2[A[j]] += 1
    # A[i] が i であるものの個数
    # A[j] が j であるものの個数
    # の積
    ans = 0
    for i in range(1, N + 1):
        ans += count[i] * count2[i]
    print(ans)

if __name__ == '__main__':
    main()