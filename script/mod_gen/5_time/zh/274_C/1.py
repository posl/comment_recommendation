def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = [0] * (2*N+1)
    for i in range(N):
        ans[A[i]] = i+1
    for i in range(1, 2*N):
        if ans[i] == 0:
            ans[i] = ans[i//2] + 1
    print('\n'.join(map(str, ans[1:])))

if __name__ == '__main__':
    main()