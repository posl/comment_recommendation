def main():
    N, M, Q = map(int, input().split())
    # 区間のリストを作成
    interval = []
    for _ in range(M):
        l, r = map(int, input().split())
        interval.append([l, r])
    # 区間のリストをソート
    interval.sort()
    # クエリのリストを作成
    query = []
    for _ in range(Q):
        p, q = map(int, input().split())
        query.append([p, q])
    # クエリのリストをソート
    query.sort(key=lambda x: x[1])
    # クエリのリストを走査
    for p, q in query:
        # 区間のリストを走査
        cnt = 0
        for l, r in interval:
            # 区間のリストの区間が, クエリのリストの区間に含まれているかを判定
            if l <= p and q <= r:
                cnt += 1
        print(cnt)
