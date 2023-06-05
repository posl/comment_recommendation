def get_max_score(n, k, p_list, c_list):
    # 从某个方格开始，最多走k步后的最大分数
    max_score = -1000000000000000
    for i in range(0, n):
        # 从第i个方格开始
        score = 0
        # 第一步
        score += c_list[p_list[i]-1]
        # 第二步
        score += c_list[p_list[p_list[i]-1]-1]
        if score > max_score:
            max_score = score
        # 第三步
        score += c_list[p_list[p_list[p_list[i]-1]-1]-1]
        if score > max_score:
            max_score = score
    return max_score

if __name__ == '__main__':
    get_max_score()