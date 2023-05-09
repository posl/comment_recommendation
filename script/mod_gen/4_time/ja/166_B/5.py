def main():
    N, K = map(int, input().split())
    A = []
    for i in range(K):
        d = int(input())
        A.append(list(map(int, input().split())))
    A = sum(A, [])
    cnt = 0
    for i in range(1, N+1):
        if i not in A:
            cnt += 1
    print(cnt)

if __name__ == '__main__':
    main()