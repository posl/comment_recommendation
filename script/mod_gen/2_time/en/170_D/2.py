def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    ans = 0
    for i in range(N-1):
        if A[i] == A[i+1]:
            continue
        if A[i+1] % A[i] != 0:
            ans += 1
    print(ans + 1)

if __name__ == '__main__':
    main()