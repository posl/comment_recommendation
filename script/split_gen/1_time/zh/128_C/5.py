def get_switch_status(n, m, k, s, p):
    # n:开关个数
    # m:灯泡个数
    # k:灯泡与开关的关联关系
    # s:开关与灯泡的关联关系
    # p:开关状态
    # 灯泡i与k_i个开关相连：开关s_{i1}，s_{i2}，...，和s_{ik_i}。当这些开关中 "开 "的开关数与p_i的模数一致时，它就被点亮。
    # 有多少种开关的 "开 "和 "关 "状态的组合可以点亮所有的灯泡？
    # 灯泡状态
    bulb_status = [0] * m
    # 开关状态
    switch_status = [0] * n
    # 开关与灯泡的关联关系
    switch_bulb = {}
    for i in range(m):
        switch_bulb[i + 1] = s[i]
    # 灯泡与开关的关联关系
    bulb_switch = {}
    for i in range(n):
        bulb_switch[i + 1] = k[i]
    # 开关状态组合
    switch_status_combination = []
    # 灯泡状态组合
    bulb_status_combination = []
    # 灯泡与开关的关联关系组合
    bulb_switch_combination = []
    # 开关与灯泡的关联关系组合
    switch_bulb_combination = []
    # 灯泡状态组合
    bulb_status_combination = get_status_combination(bulb_status, bulb_status_combination)
    # 灯泡与开关的关联关系组合
    bulb_switch_combination = get_combination(bulb_switch_combination, bulb_switch)
    # 开关与灯泡的关联关系组合
    switch_bulb_combination = get_combination(switch_bulb_combination, switch_bulb)
    # 开关状态组合
