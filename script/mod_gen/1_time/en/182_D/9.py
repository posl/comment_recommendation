def main():
    N = int(input())
    A = list(map(int, input().split()))
    #A = [2, -1, -2]
    #N = len(A)
    ans = 0
    for i in range(N):
        ans += A[i]
        if ans < 0:
            ans = 0
    print(ans)

if __name__ == '__main__':
    main()