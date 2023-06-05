def main():
    #读取输入
    n = int(input())
    a_b = []
    for i in range(n):
        a_b.append(list(map(int,input().split())))
    #按照最后期限排序
    a_b.sort(key=lambda x:x[1])
    #计算完成时间
    time = 0
    for i in range(n):
        time += a_b[i][0]
        if time > a_b[i][1]:
            print("No")
            return
    print("Yes")
