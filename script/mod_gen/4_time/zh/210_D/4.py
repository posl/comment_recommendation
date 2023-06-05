def get_min_cost(h, w, c, a):
    min_cost = 10**9 * 10**9
    # 从左上角开始遍历
    for i in range(h):
        for j in range(w):
            # 从右下角开始遍历
            for k in range(h-1, i-1, -1):
                for l in range(w-1, j-1, -1):
                    # 计算建站花费
                    cost = a[i][j] + a[k][l]
                    # 计算建轨道花费
                    cost += c * (abs(i-k) + abs(j-l))
                    min_cost = min(min_cost, cost)
    return min_cost

if __name__ == '__main__':
    get_min_cost()