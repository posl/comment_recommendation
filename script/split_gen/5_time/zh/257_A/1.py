def get_char(n, x):
    # 从字符串的开头找出第X个字符，这个字符串是由这些字符串联而成的：A的N份，B的N份，...，Z的N份，按这个顺序排列。
    # 1 ≦ N ≦ 100
    # 1 ≦ X ≦ N× 26
    # 输入的所有数值都是整数。
    # 输入是由标准输入提供的，格式如下：
    # N X
    # 打印答案。
    # 输入样本 1
    # 1 3
    # 样本输出 1
    # C
    # 我们得到字符串ABCDEFGHIJKLMNOPQRSTUVWXYZ，其从头开始的第3个字符是C。
    # 输入样本2
    # 2 12
    # 样本输出 2
    # F
    # 我们得到字符串AABBCCDDEEFFGGHHIIJKKLLMMNNOOPPQQRRSSTTUUVVWWXXYYZZ，其从头开始的第12个字符是F。
    # print(n, x)
    if n < 1 or n > 100:
        return
    if x < 1 or x > n * 26:
        return
    # 字母表
    alp = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    # print(alp)
    # 重复N次
    alp = alp * n
    # print(alp)
    # 获取第x个字符
    return alp[x - 1]
