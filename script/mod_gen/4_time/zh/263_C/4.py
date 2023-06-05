def print_all_sequences(n,m):
    """
    打印所有长度为N的严格递增的整数序列，其中所有元素都在1到M之间（包括），按词典上的升序排列。
    :param n: 序列长度
    :param m: 序列元素最大值
    :return:
    """
    def print_sequence(seq):
        """
        打印序列
        :param seq:
        :return:
        """
        for i in range(len(seq)):
            print(seq[i],end=" ")
        print("")
    def print_all_sequences_helper(seq, i):
        """
        打印所有长度为N的严格递增的整数序列，其中所有元素都在1到M之间（包括），按词典上的升序排列。
        :param seq: 保存序列的数组
        :param i: 当前正在处理的元素的下标
        :return:
        """
        if i == n:
            print_sequence(seq)
            return
        # 从前一个元素的值加1开始，到m结束
        for j in range(1 if i == 0 else seq[i-1]+1,m+1):
            seq[i] = j
            print_all_sequences_helper(seq,i+1)
    seq = [0] * n
    print_all_sequences_helper(seq,0)
