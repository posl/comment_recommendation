def main():
    #输入
    n,m = map(int,input().split())
    #初始值
    p = [0]*n
    s = [0]*n
    #输入
    for i in range(m):
        p[i],s[i] = map(str,input().split())
        p[i] = int(p[i])
    #初始值
    ans = 0
    pen = 0
    #循环
    for i in range(n):
        #如果答案正确
        if s[i] == "AC":
            #答案正确的问题数+1
            ans += 1
            #罚时加上该问题的罚时
            pen += p[i]
        #如果答案错误
        else:
            #并且该问题的答案已经错误过一次
            if p[i] in p[:i]:
                #罚时加上20
                pen += 20
    #输出
    print(ans,pen)

if __name__ == '__main__':
    main()