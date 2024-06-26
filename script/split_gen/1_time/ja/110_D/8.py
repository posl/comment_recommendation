def solve(n, m):
    # mの素因数分解
    # m = p_1^r_1 * p_2^r_2 * ... * p_k^r_k
    # という形で表せる。
    # ここで、p_iはmの約数で、r_iはp_iの指数である。
    # このとき、a_1 * a_2 * ... * a_n = m となる正整数からなる長さnの数列aは
    # r_1 + r_2 + ... + r_k 通り存在する。
    # なぜなら、a_1 = p_1^x_1, a_2 = p_2^x_2, ... , a_k = p_k^x_k
    # とすると、a_i = p_i^x_i であるから、
    # a_1 * a_2 * ... * a_n = m となる。
    # また、この時、a_1, a_2, ... , a_nはすべて異なる。
    # なぜなら、x_1, x_2, ... , x_kのいずれかが同じであると、
    # a_1 * a_2 * ... * a_n = p_1^x_1 * p_2^x_2 * ... * p_k^x_k
    # = p_1^(x_1+x_2+...+x_k) * p_2^(x_1+x_2+...+x_k) * ... * p_k^(x_1+x_2+...+x_k)
    # = p_1^(x_1+x_2+...+x_k) * p_2^(x_1+x_2+...+x_k) * ... * p_k^(x_1+x_2+...+x_k)
    # = p_1^r_1 * p_2^r_2 * ... * p_k^r_k
    # = m
    # となってしまうからである。
    # したがって、a_1
