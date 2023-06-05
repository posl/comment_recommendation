def g1(x):
    #将x的十进制数字按降序重新排列而得到的整数
    #例如，我们有g_1（314）=431
    #注意，前导零被忽略。
    x = str(x)
    x = list(x)
    x.sort(reverse=True)
    x = "".join(x)
    x = int(x)
    return x

if __name__ == '__main__':
    g1()