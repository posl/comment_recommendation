def main():
    #入力
    N = int(input())
    S = list(map(int,input().split()))
    #解答
    ans = 0
    for i in range(N):
        for a in range(1,1001):
            for b in range(1,1001):
                if S[i] == 4*a*b+3*a+3*b:
                    break
            else:
                continue
            break
        else:
            ans += 1
    print(ans)
