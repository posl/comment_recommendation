def main():
    N = int(input())
    A = list(map(int, input().split()))
    A = [a-1 for a in A]
    if A[0] != 0:
        print(-1)
        return
    ans = 0
    for i in range(1, N):
        if A[i] == 0:
            ans += 1
            continue
        if A[i] < A[i-1]:
            print(-1)
            return
        if A[i] == A[i-1]:
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()