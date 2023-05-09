def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    ans = A[0]
    for i in range(1, N):
        if ans < A[i]:
            ans = A[i] - ans
        else:
            ans = A[i]
    print(ans)

if __name__ == '__main__':
    main()