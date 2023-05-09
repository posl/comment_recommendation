def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = [0] * (2 * N + 1)
    for i in range(N):
        ans[A[i]] = 1
    for i in range(N):
        if ans[2 * A[i]] == 1:
            ans[2 * A[i] + 1] = ans[A[i]] + 1
        else:
            ans[2 * A[i]] = ans[A[i]] + 1
    print('
'.join(map(str, ans)))

if __name__ == '__main__':
    main()