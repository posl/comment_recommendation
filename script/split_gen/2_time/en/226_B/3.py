def main():
    N = int(input())
    dic = {}
    for i in range(N):
        S = [int(x) for x in input().split()]
        L = S[0]
        S = S[1:]
        if L in dic:
            dic[L].append(S)
        else:
            dic[L] = [S]
    ans = 0
    for L in dic:
        dic[L] = set([tuple(x) for x in dic[L]])
        ans += len(dic[L])
    print(ans)
