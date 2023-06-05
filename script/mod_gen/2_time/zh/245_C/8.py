def main():
    n = int(input())
    A = list(map(int, input().split()))
    A.sort()
    ans = 0
    for i in range(n):
        if A[i] <= ans:
            ans += A[i]
        else:
            break
    print(ans)

if __name__ == '__main__':
    main()