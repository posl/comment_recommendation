def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    i = 0
    j = 0
    count = 0
    ans = [0] * N
    while i < N:
        if A[i] == A[j]:
            count += 1
            i += 1
        else:
            ans[count - 1] += 1
            count = 0
            j = i
    ans[count - 1] += 1
    for i in range(N):
        print(ans[i])

if __name__ == '__main__':
    main()