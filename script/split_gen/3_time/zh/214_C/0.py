def find_first_time(N, S, T):
    # Snuke i（1 ≦ i ≦ N）在时间t收到一颗宝石，S_i单位的时间后，它将在时间t+S_i将该宝石交给Snuke i+1
    # 高桥将在时间T_i递给Snuke i一颗宝石。
    # 对于每个i（1 ≦ i ≦ N），找出Snuke i第一次收到宝石的时间
    # 按照时间顺序列出Snuke三人和Takahashi到时间13为止的行动。
    # 时间3：高桥将一颗宝石交给Snuke 1。
    # 时间7：斯诺克1把宝石交给斯诺克2。
    # 时间8：Snuke 2将一颗宝石交给Snuke 3。
    # 时间10：高桥将一颗宝石交给Snuke 2。
    # 时间11：Snuke 2递给Snuke 3一颗宝石。
    # 时间13：Snuke 3将一颗宝石交给Snuke 1。
    # 此后，他们将继续递送宝石，尽管这与答案无关。
    # 请注意，S_i和T_i的值可能不是不同的。
    # 请注意，一个Snuke可以同时进行多个交易。特别是，一个Snuke可以同时从高桥和另一个Snuke那里接收宝石。
    # 请注意，Snuke i（1 ≦ i ≦ N）在时间t收到一颗宝石，S_i单位的时间后，它将在时间t+S_i将该宝石交给Snuke i+1。
    # 此外，高桥将在时间T_i递给Snuke i一颗
