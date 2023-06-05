def main():
    # 读取输入
    n,m = map(int,input().split())
    # 保存输入
    s = []
    c = []
    # 读取输入
    for i in range(m):
        s_temp,c_temp = map(int,input().split())
        s.append(s_temp)
        c.append(c_temp)
    # 得到结果
    result = get_result(n,m,s,c)
    # 打印结果
    print(result)
