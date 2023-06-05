def main():
    n,k = map(int,input().split())
    sushi = []
    for _ in range(n):
        t,d = map(int,input().split())
        sushi.append((t,d))
    sushi.sort(key=lambda x:x[1],reverse=True)
    sushi.sort(key=lambda x:x[0])
    # print(sushi)
    # 配列tに寿司の種類を入れる
    t = []
    for i in range(n):
        t.append(sushi[i][0])
    # 配列dに寿司の美味しさを入れる
    d = []
    for i in range(n):
        d.append(sushi[i][1])
    # print(t)
    # print(d)
    # 配列dicに寿司の美味しさを入れる
    dic = {}
    for i in range(n):
        if t[i] in dic.keys():
            dic[t[i]].append(d[i])
        else:
            dic[t[i]] = [d[i]]
    # print(dic)
    # 配列d2に各種類の寿司の美味しさの最大値を入れる
    d2 = []
    for i in range(1,n+1):
        d2.append(max(dic[i]))
    # print(d2)
    # 配列d3に各種類の寿司の美味しさの最大値を降順に入れる
    d3 = sorted(d2,reverse=True)
    # print(d3)
    # 配列d4に各種類の寿司の美味しさの最大値の累積和を入れる
    d4 = []
    d4.append(d3[0])
    for i in range(1,n):
        d4.append(d4[i-1]+d3[i])
    # print(d4)
    # 配列d5に各種類の寿司の美味しさの最大値の累積和の最大値を入れる
    d5 = []
    for i in range(k-1,n):
        d5.append(d4[i])
