def main():
    n = int(input())
    # 用于记录原始提交物的字典
    # key:字符串，value:最早提交的索引
    original_submissions = {}
    # 用于记录最佳提交物的字典
    # key:字符串，value:最早提交的索引
    best_submissions = {}
    for i in range(n):
        # 获取输入的字符串和分数
        s, t = input().split()
        t = int(t)
        # 如果是原始提交物，则记录
        if s not in original_submissions:
            original_submissions[s] = i
        # 如果是最佳提交物，则记录
        if s not in best_submissions or t > best_submissions[s][1]:
            best_submissions[s] = [i, t]
    # 获取最佳提交物的索引
    best_submission = min(best_submissions.items(), key=lambda x: (x[1][1], x[1][0]))
    # 输出最佳提交物的索引
    print(best_submission[1][0] + 1)
