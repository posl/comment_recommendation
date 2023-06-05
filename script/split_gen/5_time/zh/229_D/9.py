def main():
    # 输入
    S = input()
    K = int(input())
    # 处理
    # 用 . 分割 S
    # 用列表存储分割后的结果
    s_list = S.split('.')
    # 用列表存储每个 . 之间的 X 的数量
    x_list = []
    for i in s_list:
        x_list.append(len(i))
    # 如果 s_list[0] 为空，说明 s_list[0] 前面没有 X，所以删除 x_list[0]
    if x_list[0] == 0:
        x_list.pop(0)
    # 如果 s_list[-1] 为空，说明 s_list[-1] 后面没有 X，所以删除 x_list[-1]
    if x_list[-1] == 0:
        x_list.pop(-1)
    # 如果没有 X，输出 0
    if len(x_list) == 0:
        print(0)
        exit()
    # 如果 K 大于等于 len(x_list)，说明可以将所有的 . 都替换为 X
    if K >= len(x_list):
        print(len(S))
        exit()
    # 如果 K 小于 len(x_list)，说明可以将 K 个 . 都替换为 X
    # 但是这 K 个 . 不能相邻，否则会有 K+1 个连续的 X
    # 所以将 K 个 . 替换为 X 后，会有 K+1 个连续的 X
    # 所以最多有 K+1 个连续的 X
    # 所以输出 K+1
    if K < len(x_list):
        print(K+1)
        exit()
