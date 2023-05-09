def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    ans = 0
    if A[0] < 0:
        for i in range(N):
            ans += -A[i]
    else:
        for i in range(N):
            ans += A[i]
        if A[0] == 0:
            pass
        elif A[0] > 0:
            ans -= 2*A[0]
        else:
            ans += 2*A[0]
    print(ans)
main()

if __name__ == '__main__':
    main()