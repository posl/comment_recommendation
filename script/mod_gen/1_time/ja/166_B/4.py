def main():
    N, K = map(int, input().split())
    d = []
    A = []
    for i in range(K):
        d.append(int(input()))
        A.append(list(map(int, input().split())))
    ans = 0
    for i in range(N):
        for j in range(K):
            if i+1 in A[j]:
                break
        else:
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()