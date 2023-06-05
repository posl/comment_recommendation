def main():
    # 读取输入
    n = int(input())
    ab_list = []
    for i in range(n):
        ab_list.append(list(map(int, input().split())))
    ab_list.sort(key=lambda x:x[1])
    # 计算
    time = 0
    for i in range(n):
        time += ab_list[i][0]
        if time > ab_list[i][1]:
            print("No")
            return
    print("Yes")
