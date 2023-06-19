def main():
    # 读取输入
    s = []
    for i in range(10):
        s.append(input())
    # 找到A,B,C,D
    for A in range(1, 11):
        for B in range(A, 11):
            for C in range(1, 11):
                for D in range(C, 11):
                    # 检查是否满足条件
                    flag = True
                    for i in range(A-1, B):
                        for j in range(C-1, D):
                            if s[i][j] != '#':
                                flag = False
                                break
                        if not flag:
                            break
                    if flag:
                        print(A, B)
                        print(C, D)
                        return
