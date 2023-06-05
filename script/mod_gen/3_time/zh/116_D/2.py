def solve():
    # 读取输入
    N, K = map(int, input().split())
    sushi = []
    for i in range(N):
        t, d = map(int, input().split())
        sushi.append((t, d))
    sushi.sort(key=lambda x: x[1], reverse=True)
    # print(sushi)
    # 选出美味度最大的K个寿司
    # 选出来的寿司的种类
    kinds = set()
    # 选出来的寿司的美味度之和
    sum_d = 0
    # 选出来的寿司的美味度之和的平方
    sum_d2 = 0
    # 选出来的寿司的种类数
    kinds_num = 0
    # 选出来的寿司的种类数的平方
    kinds_num2 = 0
    for i in range(K):
        t, d = sushi[i]
        kinds.add(t)
        sum_d += d
        sum_d2 += d * d
    kinds_num = len(kinds)
    kinds_num2 = kinds_num * kinds_num
    # print(kinds_num, kinds_num2)
    # print(sum_d, sum_d2)
    # 满意度
    ans = sum_d2 + kinds_num2
    # print(ans)
    # 选出最大的满意度
    for i in range(K, N):
        t, d = sushi[i]
        # print(t, d)
        if t in kinds:
            continue
        # print(kinds)
        kinds_num += 1
        kinds_num2 = kinds_num * kinds_num
        sum_d2 = sum_d2 - d * d + sum_d * 2 * d + d * d
        # print(kinds_num, kinds_num2)
        # print(sum_d, sum_d2)
        ans = max(ans, sum_d2 + kinds_num2)
        # print(ans)
        kinds.add(t)
    print(ans)

if __name__ == '__main__':
    solve()