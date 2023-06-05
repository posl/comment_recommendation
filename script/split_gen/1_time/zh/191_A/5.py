def main():
    # 读取输入
    input = raw_input()
    # 读取输入，分割成列表
    input_list = input.split(' ')
    # 把列表里的元素转换成整数
    input_list = [int(x) for x in input_list]
    # 把列表里的元素赋值给变量
    V,T,S,D = input_list
    # 计算球飞行的距离
    distance = V*T
    # 判断是否能被击中
    if distance <= D <= V*S:
        print 'No'
    else:
        print 'Yes'
