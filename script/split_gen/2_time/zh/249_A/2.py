def main():
    # 读取输入
    a, b, c, d, e, f, x = map(int, input().split())
    # 高桥和青木各自的位置
    t_pos = 0
    a_pos = 0
    # 高桥和青木各自的状态
    t_state = 0
    a_state = 0
    # 高桥和青木各自的速度
    t_speed = 0
    a_speed = 0
    # 高桥和青木各自的时间
    t_time = 0
    a_time = 0
    # 高桥和青木各自的距离
    t_distance = 0
    a_distance = 0
    # 2人同时开始慢跑，直到x秒后
    while t_pos + a_pos < x:
        # 高桥的状态
        if t_state == 0:
            t_speed = b
            t_time = a
            t_state = 1
        else:
            t_speed = 0
            t_time = c
            t_state = 0
        # 青木的状态
        if a_state == 0:
            a_speed = d
            a_time = e
            a_state = 1
        else:
            a_speed = 0
            a_time = f
            a_state = 0
        # 高桥和青木各自跑的距离
        t_distance = t_speed * t_time
        a_distance = a_speed * a_time
        # 高桥和青木各自跑的距离
        t_pos += t_distance
        a_pos += a_distance
    # 高桥和青木谁在前面
    if t_pos > a_pos:
        print("高桥")
    elif t_pos < a_pos:
        print("青木")
    else:
        print("画")
