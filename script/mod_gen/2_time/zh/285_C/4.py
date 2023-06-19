def get_index(s):
    # 26个字母
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    # 26个字母的长度
    alphabet_len = len(alphabet)
    # 问题的长度
    s_len = len(s)
    # ID的索引
    index = 0
    # 每个问题的长度
    problem_len = 1
    # 问题的总长度
    problem_total_len = 0
    # 问题的总长度和问题的长度相等时，说明是最后一个问题
    while problem_total_len < s_len:
        problem_total_len += alphabet_len**problem_len
        index += alphabet_len**problem_len
        problem_len += 1
    # 问题的总长度和问题的长度相等时，说明是最后一个问题，所以减去一个问题的长度
    index -= alphabet_len**(problem_len-1)
    # 问题的总长度和问题的长度相等时，说明是最后一个问题，所以减去一个问题的长度
    problem_total_len -= alphabet_len**(problem_len-1)
    # 问题的长度
    problem_len -= 1
    # 问题的总长度和问题的长度相等时，说明是最后一个问题，所以减去一个问题的长度
    problem_total_len -= alphabet_len**(problem_len-1)
    # 问题的长度
    problem_len -= 1
    # 问题的长度
    problem_len -= 1
    # 问题的总长度和问题的长度相等时，说明是最后一个问题，所以减去一个问题的长度
    problem_total_len -= alphabet_len**(problem_len-1)
    # 问题的长度
    problem_len -= 1
    # 问题的长度
    problem_len -= 1
    # 问题的总长度和问题的长度相等时，说明是最后一个问题，所以减去一个问题的长度
    problem_total_len -= alphabet_len**(problem_len-1)
    # 问题的长度
    problem_len -= 1
    # 问题的长度
    problem_len -= 1
    # 问题的总长度和问题的长度相等时，说明是最后一个问题，所

if __name__ == '__main__':
    get_index()