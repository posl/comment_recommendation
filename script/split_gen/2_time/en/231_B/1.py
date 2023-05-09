def main():
    #input
    N = int(input())
    S = [input() for _ in range(N)]
    #compute
    dic = {}
    for s in S:
        dic[s] = dic.get(s, 0) + 1
    ans = max(dic, key=dic.get)
    #output
    print(ans)
