def main():
    #获取输入数据
    input_str = input()
    input_list = input_str.split()
    N = int(input_list[0])
    A = int(input_list[1])
    B = int(input_list[2])
    input_str = input()
    input_list = input_str.split()
    P = int(input_list[0])
    Q = int(input_list[1])
    R = int(input_list[2])
    S = int(input_list[3])
    #计算输出数据
    #生成网格
    grid = []
    for i in range(N):
        grid.append([0]*N)
    #涂色
    for k in range(max(1-A,1-B),min(N-A,N-B)+1):
        grid[A+k-1][B+k-1] = 1
    for k in range(max(1-A,B-N),min(N-A,B-1)+1):
        grid[A+k-1][B-k-1] = 1
    #统计输出数据
    output_list = []
    for i in range(P-1,Q):
        output_str = ""
        for j in range(R-1,S):
            if grid[i][j] == 1:
                output_str += "#"
            else:
                output_str += "."
        output_list.append(output_str)
    #输出
    for output_str in output_list:
        print(output_str)

if __name__ == '__main__':
    main()