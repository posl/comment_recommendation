def main():
    #input
    N, K = map(int, input().split())
    S = [input() for _ in range(N)]
    #solve
    #bit全探索
    ans = 0
    for i in range(1<<26):
        cnt = 0
        for s in S:
            flag = True
            for j in s:
                if not(i&(1<<(ord(j)-97))):
                    flag = False
                    break
            if flag:
                cnt += 1
        if cnt >= K:
            ans = max(ans, bin(i).count("1"))
    #output
    print(ans)
