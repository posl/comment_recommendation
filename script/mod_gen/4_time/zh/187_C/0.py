def main():
    # 读取输入
    N = int(input())
    S = []
    for i in range(N):
        S.append(input())
    # 解决问题
    # 1. 检查是否有重复元素
    # 2. 检查是否有元素和它的逆元素
    S_set = set(S)
    if len(S_

if __name__ == '__main__':
    main()