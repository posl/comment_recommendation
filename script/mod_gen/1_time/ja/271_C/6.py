def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    if A[0] != 1:
        print(0)
        return
    if N == 1:
        print(0)
        return
    ans = 1
    for i in range(N-1):
        if A[i+1] - A[i] > 1:
            break
        ans += 1
    print(ans)

if __name__ == '__main__':
    main()