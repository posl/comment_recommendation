def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    ans = 0
    i = 0
    while i < N:
        if i == N - 1 or A[i] != A[i + 1]:
            i += 1
        else:
            ans += 1
            i += 2
    print(ans)

if __name__ == '__main__':
    main()