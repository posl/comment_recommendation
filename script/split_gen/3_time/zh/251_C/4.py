def main():
    n = int(input())
    dic = {}
    for i in range(n):
        s, t = input().split()
        if s in dic:
            dic[s] = min(dic[s], int(t))
        else:
            dic[s] = int(t)
    dic = sorted(dic.items(), key=lambda x: x[1], reverse=True)
    print([i for i, j in enumerate(dic) if j[1] == dic[0][1]][0] + 1)
