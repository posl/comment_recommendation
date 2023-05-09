def main():
    N,Q = map(int,input().split())
    A = list(map(int,input().split()))
    X = [int(input()) for _ in range(Q)]
    A.sort()
    A.append(10**10)
    ans = []
    for x in X:
        cnt = 0
        left = 0
        right = N
        while left < right:
            mid = (left+right) // 2
            if A[mid] <= x:
                left = mid + 1
            else:
                right = mid
        cnt += (N-left)*x
        for i in range(left):
            cnt += x-A[i]
        ans.append(cnt)
    for i in ans:
        print(i)

if __name__ == '__main__':
    main()