def main():
    #入力
    N, K = map(int, input().split())
    V = list(map(int, input().split()))
    #解答
    ans = 0
    for i in range(K+1):
        for j in range(K+1-i):
            if i+j > N:
                continue
            tmp = V[:i] + V[-j:]
            tmp.sort()
            for k in range(K-i-j):
                if len(tmp) == 0:
                    break
                if tmp[0] < 0:
                    tmp.pop(0)
                else:
                    break
            ans = max(ans, sum(tmp))
    print(ans)
