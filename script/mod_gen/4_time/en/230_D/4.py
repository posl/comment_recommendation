def main():
    N, D = map(int, input().split())
    L = [0] * N
    R = [0] * N
    for i in range(N):
        L[i], R[i] = map(int, input().split())
    L.sort()
    R.sort()
    i = 0
    j = 0
    ans = 0
    while i < N:
        while j < N and R[j] < L[i]:
            j += 1
        ans += 1
        i = i + j + D
    print(ans)
main()

if __name__ == '__main__':
    main()