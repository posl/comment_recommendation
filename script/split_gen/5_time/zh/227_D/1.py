def main():
    # 读入数据
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    # 求解
    # 每个部门的人数
    department = [0] * n
    for i in range(n):
        department[a[i] - 1] += 1
    # 每个部门的人数对应的部门数
    count = [0] * n
    for i in range(n):
        count[department[i] - 1] += 1
    # 部门数
    department_num = n
    # 项目数
    project_num = 0
    # 从部门数最多的部门开始
    for i in range(n - 1, -1, -1):
        # 如果部门数为0，结束
        if department_num == 0:
            break
        # 如果部门人数为0，跳过
        if count[i] == 0:
            continue
        # 如果部门人数不足，结束
        if count[i] < k:
            break
        # 计算项目数
        project_num += count[i] // k
        # 减少部门数
        department_num -= count[i]
        # 减少部门人数
        count[i - 1] += count[i] % k
    # 输出
    print(project_num)
