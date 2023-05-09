def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N//2):
        if A[i] == A[N-1-i]:
            continue
        elif A[i] == A[i+1] and A[i+1] == A[N-1-i-1]:
            ans += 1
        else:
            ans += 2
    if N % 2 == 1 and A[N//2] != A[N//2+1]:
        ans += 1
    print(ans)

if __name__ == '__main__':
    main()