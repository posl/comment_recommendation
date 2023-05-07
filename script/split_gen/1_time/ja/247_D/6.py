def main():
    # 入力
    Q = int(input())
    query = [list(map(int, input().split())) for _ in range(Q)]
    # 処理
    sum = 0
    left = []
    right = []
    for i in range(Q):
        if query[i][0] == 1:
            right.append(query[i][1])
            sum += query[i][1] * query[i][2]
        else:
            for j in range(query[i][1]):
                if len(left) == 0:
                    left.append(right.pop(0))
                else:
                    left.pop(0)
            sum -= sum(left)
    # 出力
    print(sum)
