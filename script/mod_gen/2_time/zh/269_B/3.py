def main():
    #读取输入数据
    strs = []
    for i in range(10):
        strs.append(input())
    # print(strs)
    #找出A,B,C,D
    A, B, C, D = 0, 0, 0, 0
    for i in range(10):
        if strs[i].find('#') != -1:
            A = i + 1
            B = i + 1
            break
    for i in range(A, 10):
        if strs[i].find('#') == -1:
            B = i
            break
    for i in range(10):
        if strs[i].find('#') != -1:
            C = strs[i].find('#') + 1
            D = strs[i].find('#') + 1
            break
    for i in range(C, 10):
        if strs[i].find('#') == -1:
            D = strs[i].find('#')
            break
    # print(A, B, C, D)
    print(A, B)
    print(C, D)

if __name__ == '__main__':
    main()