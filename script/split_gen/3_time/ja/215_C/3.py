def main():
    S, K = input().split()
    K = int(K)
    S = sorted(S)
    ans = []
    while True:
        if len(S) == 0:
            break
        tmp = len(S)
        for i in range(1, len(S)):
            tmp = tmp * i
            if tmp >= K:
                ans.append(S[i-1])
                K = K - (tmp // i)
                S.pop(i-1)
                break
        else:
            ans.append(S[-1])
            S.pop()
    print("".join(ans))
