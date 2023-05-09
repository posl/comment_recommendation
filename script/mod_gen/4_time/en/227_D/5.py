def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    #print(A)
    ans = 0
    for i in range(K):
        ans += A[i]
    print(ans)
    return

if __name__ == '__main__':
    main()