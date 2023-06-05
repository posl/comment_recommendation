def main():
    # 读入数据
    s = input()
    # 解决问题
    n = len(s)
    # 从左向右扫描，记录从左向右的第一个R的位置
    rpos = 0
    while rpos < n and s[rpos] != 'R':
        rpos += 1
    # 从左向右扫描，记录从右向左的第一个L的位置
    lpos = n - 1
    while lpos >= 0 and s[lpos] != 'L':
        lpos -= 1
    # 从左向右扫描，记录每个L的位置
    lpos_list = []
    for i in range(n):
        if s[i] == 'L':
            lpos_list.append(i)
    # 从右向左扫描，记录每个R的位置
    rpos_list = []
    for i in range(n - 1, -1, -1):
        if s[i] == 'R':
            rpos_list.append(i)
    # 计算每个孩子的位置
    pos = [0] * n
    for i in range(len(lpos_list)):
        pos[lpos_list[i]] = i + 1
    for i in range(len(rpos_list)):
        pos[rpos_list[i]] = i + 1
    # 计算每个孩子的移动次数
    move = [0] * n
    for i in range(len(lpos_list)):
        move[lpos_list[i]] = lpos_list[i] - rpos_list[i] - 1
    for i in range(len(rpos_list)):
        move[rpos_list[i]] = rpos_list[i] - lpos_list[i] - 1
    # 计算每个孩子的最终位置
    final_pos = [0] * n
    for i in range(n):
        final_pos[i] = pos[i] + move[i]
    # 计算每个孩子的最终位置上站的孩子的数量
    ans = [0] * n
    for i in range(n):
        ans[final_pos[i] - 1] += 1
