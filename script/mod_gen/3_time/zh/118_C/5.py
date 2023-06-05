def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    ans = A[0]
    for i in range(1, N):
        if ans * 2 >= A[i]:
            ans += A[i]
        else:
            ans = A[i]
    print(ans)

if __name__ == '__main__':
    main()