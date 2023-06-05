def main():
    N = int(input())
    S = input()
    W = list(map(int, input().split()))
    W.sort(reverse=True)
    # print(N, S, W)
    # print(S.count('0'), S.count('1'))
    # print(W)
    def check(x):
        # print(x)
        cnt = 0
        for i in range(N):
            if S[i] == '0' and W[i] <= x:
                cnt += 1
            elif S[i] == '1' and W[i] > x:
                cnt += 1
        # print(cnt)
        return cnt
    def bin_search():
        left = -1
        right = 10**9+1
        while right - left > 1:
            mid = (left + right) // 2
            if check(mid) >= N // 2 + 1:
                right = mid
            else:
                left = mid
        return right
    print(bin_search())

if __name__ == '__main__':
    main()