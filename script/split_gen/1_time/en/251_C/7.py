def main():
    N = int(input())
    dic = {}
    for i in range(N):
        s,t = input().split()
        t = int(t)
        if s in dic:
            if t > dic[s][0]:
                dic[s] = (t,i)
        else:
            dic[s] = (t,i)
    print(min(dic.values())[1]+1)
