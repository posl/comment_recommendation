def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    A.append(10**9+1)
    ans = [0] * N
    cnt = 0
    for i in range(N):
        cnt += 1
        if A[i] != A[i+1]:
            ans[cnt-1] += 1
            cnt = 0
    print('\n'.join(map(str, ans)))

if __name__ == '__main__':
    main()