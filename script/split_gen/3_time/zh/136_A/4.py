def water_transfer(A,B,C):
    # A: 1号瓶最多可以装A毫升的水
    # B: 1号瓶中有B毫升的水
    # C: 2号瓶中有C毫升的水
    # 2号瓶中最多可以装A-B毫升的水
    # 每次转移水的量为B
    # 转移次数为C//B
    # 2号瓶中的水量为C-C//B*B
    return C-C//B*B
