def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = [0] * N
    for i in range(N):
        ans[i] = (A[i] - A[i - 1]) // 2
    ans[0] += sum(A)
    ans = [str(a) for a in ans]
    print(' '.join(ans))

if __name__ == '__main__':
    main()