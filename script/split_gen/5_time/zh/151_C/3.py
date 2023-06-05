def main():
    #第一行输入
    n, m = map(int, input().split())
    #初始化题目状态
    p = [0]*n
    s = [0]*n
    #记录AC的题目数
    ac = 0
    #记录罚分
    wa = 0
    for i in range(m):
        #输入题号和状态
        pi, si = input().split()
        pi = int(pi)
        #如果是AC
        if si == "AC":
            #如果之前没AC过
            if s[pi-1] == 0:
                #AC题目数+1
                ac += 1
                #罚分+之前WA的数量
                wa += p[pi-1]
                #标记AC
                s[pi-1] = 1
        #如果是WA
        else:
            #之前没AC过
            if s[pi-1] == 0:
                #WA数量+1
                p[pi-1] += 1
    #输出答案
    print(ac, wa)
