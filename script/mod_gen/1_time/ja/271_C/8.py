def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    A.append(10**9+1)
    cnt = 0
    ans = 0
    for i in range(N):
        if A[i] == A[i+1]:
            cnt += 1
            if cnt == 2:
                cnt = 0
                ans += 1
        else:
            cnt = 0
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()