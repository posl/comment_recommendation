def main():
    # 读入数据
    N, M, Q = map(int, input().split())
    trains = []
    for i in range(M):
        L, R = map(int, input().split())
        trains.append((L, R))
    queries = []
    for i in range(Q):
        p, q = map(int, input().split())
        queries.append((p, q))
    # 计算答案
    answers = []
    for p, q in queries:
        count = 0
        for L, R in trains:
            if p <= L and R <= q:
                count += 1
        answers.append(count)
    # 输出答案
    for ans in answers:
        print(ans)
