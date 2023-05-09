def main():
    N = int(input())
    A = list(map(int, input().split()))
    cnt = 0
    for i in range(N // 2):
        if A[i] == A[N - i - 1]:
            continue
        elif A[i] in A[i + 1:N - i] and A[N - i - 1] in A[i + 1:N - i]:
            cnt += 1
        else:
            cnt += 2
    print(cnt)

if __name__ == '__main__':
    main()