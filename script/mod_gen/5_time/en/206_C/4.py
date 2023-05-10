def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    cnt = 0
    i = 0
    while i < N:
        j = i + 1
        while j < N and A[i] == A[j]:
            j += 1
        cnt += (j - i) * (N - j)
        i = j
    print(cnt)

if __name__ == '__main__':
    main()