def solve():
    # 读入数据
    N = int(input())
    task = []
    for i in range(N):
        task.append(list(map(int, input().split())))
    # 按照最后期限排序
    task.sort(key=lambda x: x[1])
    # 从最后期限小的开始做
    t = 0
    for i in range(N):
        t += task[i][0]
        if t > task[i][1]:
            print("No")
            return
    print("Yes")
solve()
