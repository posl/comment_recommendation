def main():
    N = int(input())
    A = list(map(int,input().split()))
    ans = 0
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            if A[i] % A[j] == 0:
                break
        else:
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()