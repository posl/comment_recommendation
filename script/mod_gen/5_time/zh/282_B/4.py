def main():
    # 读取输入
    input_line = input()
    input_line_list = input_line.split(" ")
    N = int(input_line_list[0])
    M = int(input_line_list[1])
    input_str_list = []
    for i in range(N):
        input_str_list.append(input())
    # print(N,M,input_str_list)
    # 处理
    count = 0
    for i in range(N):
        for j in range(i+1,N):
            # print(i,j)
            flag = True
            for k in range(M):
                if input_str_list[i][k] == "x" and input_str_list[j][k] == "x":
                    flag = False
                    break
            if flag:
                count += 1
    print(count)

if __name__ == '__main__':
    main()