def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = [0] * N
    for i in range(N):
        if i == 0:
            ans[i] = (A[i] + A[i+1]) // 2
        elif i == N - 1:
            ans[i] = (A[i] + A[0]) // 2
        else:
            ans[i] = (A[i] + A[i+1]) // 2
    for i in range(N):
        print(ans[i], end = " ")
    print()

if __name__ == '__main__':
    main()