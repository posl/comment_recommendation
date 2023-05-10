def main():
    # n: 人数
    # m: 条件数
    n, m = map(int, input().split())
    # 条件を格納する配列
    conditions = []
    # 条件を配列に格納
    for i in range(m):
        a, b = map(int, input().split())
        conditions.append([a, b])
    # 人数分の配列を作成
    people = [i for i in range(1, n + 1)]
    # 条件を満たすかどうかのフラグ
    flag = False
    # 人を並べ替える
    for i in range(n - 1):
        # 条件を満たすかどうかのフラグ
        flag = False
        # 条件を満たす人がいるかどうか
        for condition in conditions:
            # 条件を満たす人がいればフラグを立てる
            if people[i] == condition[0] and people[i + 1] == condition[1]:
                flag = True
        # 条件を満たす人がいなければ、人を並べ替える
        if not flag:
            people[i], people[i + 1] = people[i + 1], people[i]
    # 条件を満たすかどうかのフラグ
    flag = True
    # 条件を満たす人がいるかどうか
    for condition in conditions:
        # 条件を満たす人がいなければフラグを下げる
        if people[condition[0] - 1] != condition[0] or people[condition[1] - 1] != condition[1]:
            flag = False
    # 条件を満たすかどうかを出力する
    if flag:
        print('Yes')
    else:
        print('No')
