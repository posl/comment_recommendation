def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    cnt = 0
    for i in range(N):
        for j in range(N):
            if A[i] % A[j] == 0:
                for k in range(N):
                    if A[j] % A[k] == 0:
                        cnt += 1
    print(cnt)

if __name__ == '__main__':
    main()