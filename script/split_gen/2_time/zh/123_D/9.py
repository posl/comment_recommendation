def main():
    n = int(input())
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    e = int(input())
    
    # 从1到2的时间
    t1 = (n + a - 1) // a
    # 从2到3的时间
    t2 = (t1 + b - 1) // b
    # 从3到4的时间
    t3 = (t2 + c - 1) // c
    # 从4到5的时间
    t4 = (t3 + d - 1) // d
    # 从5到6的时间
    t5 = (t4 + e - 1) // e
    print(t5)
