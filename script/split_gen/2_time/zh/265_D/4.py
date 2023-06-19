def main():
    n, p, q, r = map(int, input().split())
    a = list(map(int, input().split()))
    # 从左到右扫描，记下当前最大值
    max_a = [0] * n
    max_a[0] = a[0]
    for i in range(1, n):
        max_a[i] = max(a[i], max_a[i - 1])
    # 从右到左扫描，记下当前最大值
    max_a_r = [0] * n
    max_a_r[n - 1] = a[n - 1]
    for i in range(n - 2, -1, -1):
        max_a_r[i] = max(a[i], max_a_r[i + 1])
    # 计算Q
    q_list = [0] * n
    for i in range(n):
        q_list[i] = q * a[i]
    # 计算Q
    q_list_r = [0] * n
    for i in range(n):
        q_list_r[i] = q * a[i]
    # 计算P
    p_list = [0] * n
    for i in range(n):
        p_list[i] = p * a[i]
    # 计算R
    r_list = [0] * n
    for i in range(n):
        r_list[i] = r * a[i]
    # 从左到右扫描，记下当前最大值
    max_q = [0] * n
    max_q[0] = q_list[0]
    for i in range(1, n):
        max_q[i] = max(q_list[i], max_q[i - 1])
    # 从右到左扫描，记下当前最大值
    max_q_r = [0] * n
    max_q_r[n - 1] = q_list[n - 1]
    for i in range(n - 2, -1, -1):
        max_q_r[i] = max(q_list[i], max_q_r[i + 1])
    # 从左到右扫描，记下当前最大值
    max_p = [0] * n
