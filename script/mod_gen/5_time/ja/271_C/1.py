def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    ans = 1
    for i in range(N):
        if A[i] <= ans:
            ans += A[i]
        else:
            break
    print(ans)

if __name__ == '__main__':
    main()