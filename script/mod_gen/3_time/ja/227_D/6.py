def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    A.reverse()
    cnt = 0
    for i in range(K):
        cnt += A[i]
    print(cnt)

if __name__ == '__main__':
    main()