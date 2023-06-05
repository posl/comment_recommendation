def main():
    # 读取输入
    N = int(input())
    # 从2^0开始，逐个尝试，直到找到最大的k
    k = 0
    while 2 ** k <= N:
        k += 1
    print(k - 1)
