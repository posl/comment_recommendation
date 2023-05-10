def main():
    N, T = map(int, input().split())
    A = list(map(int, input().split()))
    ans1 = T // sum(A)
    ans2 = T % sum(A)
    ans3 = 0
    for i in range(N):
        ans2 -= A[i]
        if ans2 >= 0:
            ans3 += A[i]
        else:
            break
    print(ans1 * N + i + 1, ans3 + A[i] - ans2)

if __name__ == '__main__':
    main()