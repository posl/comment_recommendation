def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    tmp = 0
    for i in range(N):
        tmp += A[i]
        ans = max(ans, tmp)
    print(ans)
main()

if __name__ == '__main__':
    main()