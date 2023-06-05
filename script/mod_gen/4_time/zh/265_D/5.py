def main():
    N, P, Q, R = map(int, input().split())
    A = list(map(int, input().split()))
    # 一开始，我认为这是一个组合问题，但是我不知道如何解决它。
    # 然后我发现，由于序列元素的限制，它可以被分解为三个子问题：
    # 1. A_x + A_{x+1}.+ ...+ A_{y-1} = P
    # 2. A_y + A_{y+1} = P+ ...+ A_{z-1} = Q
    # 3. A_z + A_{z+1} = Q+ ...+ A_{w-1} = R
    # 我们可以用动态规划来解决这个问题。
    # 我们将从左到右遍历序列，用以下变量来跟踪子问题的解决方案：
    # 1. P_left[i]：A_0 + A_1 + ... + A_i = P
    # 2. Q_left[i]：A_0 + A_1 + ... + A_i = Q
    # 3. R_left[i]：A_0 + A_1 + ... + A_i = R
    # 4. P_right[i]：A_i + A_{i+1} + ... + A_{N-1} = P
    # 5. Q_right[i]：A_i + A_{i+1} + ... + A_{N-1} = Q
    # 6. R_right[i]：A_i + A_{i+1} + ... + A_{N-1} = R
    # 我们可以通过以下方式更新这些变量：
    # 1. P_left[i] = max(P_left[i-1], A_i)
    # 2. Q_left[i] = max(Q_left[i-1], P_left[i] + A_i)
    # 3. R_left[i] = max(R_left[i-1], Q_left[i] + A_i)
    # 4. P_right[i] = max(P_right[i+1], A

if __name__ == '__main__':
    main()