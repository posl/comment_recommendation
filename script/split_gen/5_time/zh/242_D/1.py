def main():
    #读入字符串
    s = input()
    #读入查询数
    q = int(input())
    #读入查询
    query = []
    for i in range(q):
        query.append(list(map(int, input().split())))
    #处理查询
    for t, k in query:
        #计算字符串的长度
        l = len(s)
        #计算循环次数
        n = t % 3
        #循环替换
        for i in range(n):
            s = s.replace("a", "bc")
            s = s.replace("b", "ca")
            s = s.replace("c", "ab")
        #打印结果
        print(s[k-1])
