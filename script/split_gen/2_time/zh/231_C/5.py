def main():
    n = int(input())
    S = []
    for i in range(n):
        S.append(input())
    S.sort()
    #print(S)
    dic = {}
    for i in S:
        dic[i] = S.count(i)
    #print(dic)
    max_v = max(dic.values())
    for k, v in dic.items():
        if v == max_v:
            print(k)
            break
