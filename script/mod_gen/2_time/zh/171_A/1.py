def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    #print(A)
    cnt = 0
    for i in range(1, N):
        if A[i] % A[i-1] == 0:
            cnt += 1
    print(N - cnt - 1)

if __name__ == '__main__':
    main()