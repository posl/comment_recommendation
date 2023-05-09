def main():
    N = int(input())
    A = [int(x) for x in input().split()]
    ans = 0
    for i in range(N):
        while A[i] % 2 == 0:
            A[i] = A[i] / 2
            ans += 1
        while A[i] % 3 == 0:
            A[i] = A[i] / 3
            ans += 1
    for i in range(N):
        if A[i] != A[0]:
            ans = -1
    print(ans)

if __name__ == '__main__':
    main()