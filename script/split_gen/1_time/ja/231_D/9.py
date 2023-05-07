def main():
    N, M = map(int, input().split())
    # 結果はYesかNo
    result = "Yes"
    # 並び順を保持するリスト
    order = []
    # 並び順を保持するリストを初期化
    for i in range(N):
        order.append(i+1)
    # 条件を保持するリスト
    condition = []
    # 条件を保持するリストを初期化
    for i in range(M):
        A, B = map(int, input().split())
        condition.append([A, B])
    # 条件を満たしているか判定
    for i in range(M):
        A = condition[i][0]
        B = condition[i][1]
        # 並び順のリストをループ
        for j in range(N):
            # 条件を満たしているか判定
            if order[j] == A:
                # 条件を満たしている場合、並び順のリストを入れ替え
                order[j] = B
            elif order[j] == B:
                # 条件を満たしている場合、並び順のリストを入れ替え
                order[j] = A
    # 並び順のリストをループ
    for i in range(N-1):
        # 条件を満たしているか判定
        if order[i] > order[i+1]:
            # 条件を満たしていない場合、結果をNoに変更
            result = "No"
            break
    # 結果を出力
    print(result)
