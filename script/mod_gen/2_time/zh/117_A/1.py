def main():
    N,K = map(int,input().split())
    sushi = []
    for _ in range(N):
        t,d = map(int,input().split())
        sushi.append((t,d))
    sushi = sorted(sushi,key=lambda x:x[1],reverse=True)
    from collections import defaultdict
    sushi_dic = defaultdict(list)
    for i in range(N):
        sushi_dic[sushi[i][0]].append(sushi[i][1])
    sushi_dic = sorted(sushi_dic.items(),key=lambda x:len(x[1]),reverse=True)
    sushi_dic = dict(sushi_dic)
    sushi_dic = sorted(sushi_dic.items(),key=lambda x:x[1][0],reverse=True)
    sushi_dic = dict(sushi_dic)
    sushi_dic = sorted(sushi_dic.items(),key=lambda x:x[1][0],reverse=True)
    sushi_dic = dict(sushi_dic)
    # print(sushi_dic)
    ans = 0
    sushi_dic_key = list(sushi_dic.keys())
    for i in range(K):
        ans += sushi_dic[sushi_dic_key[i]][0]
    ans += (K**2)
    print(ans)

if __name__ == '__main__':
    main()