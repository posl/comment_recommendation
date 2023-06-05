def main():
    # N:学生人数
    # P:通过考试的分数
    N, P = map(int, input().split())
    # 学生成绩
    scores = list(map(int, input().split()))
    # 通过考试的学生人数
    pass_num = 0
    for score in scores:
        if score >= P:
            pass_num += 1
    # 不通过考试的学生人数
    fail_num = N - pass_num
    print(fail_num)

if __name__ == '__main__':
    main()