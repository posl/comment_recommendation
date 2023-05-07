def main():
    N = int(input())
    A = list(map(int, input().split()))
    if N == 1:
        print(0)
        return
    ans = 0
    for i in range(N//2):
        if A[i] == A[N-i-1]:
            continue
        elif A[i] == A[i+1] and A[N-i-1] == A[N-i-2]:
            ans += 1
        else:
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()