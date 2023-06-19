def main():
    # 读入N和P
    N, P = map(int, input().split())
    # 读入a_1, a_2, ..., a_N
    a = list(map(int, input().split()))
    # 用来存储能够通过考试的学生的人数
    ans = 0
    # 用来存储未能通过考试的学生的人数
    dis = 0
    # 用来存储能够通过考试的学生的人数
    for i in range(N):
        if a[i] >= P:
            ans += 1
        else:
            dis += 1
    # 输出结果
    print(dis)

if __name__ == '__main__':
    main()