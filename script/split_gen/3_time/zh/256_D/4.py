def main():
    n = int(input())
    # 读取输入
    l = []
    r = []
    for i in range(n):
        line = input()
        l.append(int(line.split()[0]))
        r.append(int(line.split()[1]))
    # 按照左端点排序
    l.sort()
    r.sort()
    # 合并区间
    ans = []
    begin = l[0]
    end = r[0]
    for i in range(1, n):
        if l[i] <= end:
            end = r[i]
        else:
            ans.append([begin, end])
            begin = l[i]
            end = r[i]
    ans.append([begin, end])
    # 打印
    for i in range(len(ans)):
        print(ans[i][0], ans[i][1])
