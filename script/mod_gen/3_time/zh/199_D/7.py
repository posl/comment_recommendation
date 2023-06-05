def get_input():
    # 获取输入
    # 输入来自标准输入，其格式如下：
    # N M
    # A_1 B_1
    # A_2 B_2
    # A_3 B_3
    # .
    # .
    # .
    # A_M B_M
    input_line = input()
    input_line = input_line.split(" ")
    N = int(input_line[0])
    M = int(input_line[1])
    # 以字典的形式保存边的信息
    edges = {}
    for i in range(0, M):
        input_line = input()
        input_line = input_line.split(" ")
        A = int(input_line[0])
        B = int(input_line[1])
        edges[i] = [A, B]
    return N, M, edges

if __name__ == '__main__':
    get_input()