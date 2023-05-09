def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    ans = [0 for i in range(N)]
    for i in range(N):
        ans[i] = A.count(A[i]) - 1
    for i in range(N):
        print(ans[i])

if __name__ == '__main__':
    main()