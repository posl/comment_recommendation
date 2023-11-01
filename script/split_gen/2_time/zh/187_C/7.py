def main():
    # 输入
    N = int(input())
    S = [input() for i in range(N)]
    # 判断
    for i in S:
        if '!' + i in S:
            print(i)
            return
    print('satisfiable')
