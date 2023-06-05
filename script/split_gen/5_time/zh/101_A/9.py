def main():
    #读入字符串
    s = input()
    #初始化结果
    result = 0
    #循环处理字符串
    for i in range(4):
        #如果是+，则加1
        if s[i] == '+':
            result += 1
        #如果是-，则减1
        else:
            result -= 1
    #打印结果
    print(result)
