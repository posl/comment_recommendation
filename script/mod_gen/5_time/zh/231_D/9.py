def main():
    # 读取输入
    N, M = map(int, input().split())
    A = []
    B = []
    for _ in range(M):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    # 从1开始，每个人的编号
    people = [i for i in range(1, N + 1)]
    # 人的编号和索引的对应关系
    people_dict = {i: i - 1 for i in people}
    # 人的索引和编号的对应关系
    people_dict_reverse = {i - 1: i for i in people}
    # 人的左右关系
    left_right_dict = {i: [i - 1, i + 1] for i in people}
    # 人的左右关系，去除边界的人
    left_right_dict[1] = [2]
    left_right_dict[N] = [N - 1]
    # 人的左右关系，去除边界的人
    for i in range(2, N):
        left_right_dict[i] = [i - 1, i + 1]
    # print(people)
    # print(people_dict)
    # print(people_dict_reverse)
    # print(left_right_dict)
    # 按照条件，依次交换位置
    for i in range(M):
        # print("第{}次交换".format(i))
        a = A[i]
        b = B[i]
        # print("交换前：", people)
        # print("交换前：", left_right_dict)
        # print("交换前：", people_dict)
        # print("交换前：", people_dict_reverse)
        # 交换位置
        # 交换人的编号
        people_dict[a], people_dict[b] = people_dict[b], people_dict[a]
        # 交换人的索引
        people_dict_reverse[people_dict[a]], people_dict_reverse[people_dict[b]] = people_dict_reverse[people_dict[b]], people_dict_reverse[people_dict[a]]
        # 交换人的左右关系
        left_right_dict[people_dict[a]], left_right_dict

if __name__ == '__main__':
    main()