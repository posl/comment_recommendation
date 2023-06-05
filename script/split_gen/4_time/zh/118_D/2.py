def main():
    #输入
    n, m = map(int, input().split())
    a_list = list(map(int, input().split()))
    #预处理
    #将数字和其对应的火柴棒数量存储在字典中
    a_dict = {}
    for i in range(m):
        a_dict[a_list[i]] = i + 1
    #将数字按照火柴棒数量排序
    a_list.sort(key=lambda x: a_dict[x], reverse=True)
    #计算数字最大长度
    max_len = n // a_dict[a_list[-1]]
    #逐位计算
    result = ''
    for i in range(max_len, 0, -1):
        for j in range(m):
            if n - a_dict[a_list[j]] == 0:
                result += str(a_list[j])
                n -= a_dict[a_list[j]]
                break
            elif n - a_dict[a_list[j]] < 0:
                continue
            elif n - a_dict[a_list[j]] > 0:
                result += str(a_list[j])
                n -= a_dict[a_list[j]]
                break
    #输出
    print(result)
