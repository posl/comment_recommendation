def main():
    import sys
    import math
    import numpy as np
    # 读取输入
    N, W = map(int, sys.stdin.readline().strip().split())
    A = np.zeros(N, dtype=np.int64)
    B = np.zeros(N, dtype=np.int64)
    for i in range(N):
        A[i], B[i] = map(int, sys.stdin.readline().strip().split())
    # 处理
    # 1. 将A和B按照A降序排序
    # 2. 将B/A按照降序排序
    # 3. 从大到小累加B/A，直到W
    # 4. 输出
    # 5. 优化：从大到小累加B/A，直到W，如果B/A大于1，则将B/A设置为1
    # 6. 优化：从大到小累加B/A，直到W，如果B/A大于1，则将B/A设置为1，如果W为奇数，且B/A小于1，则将B/A设置为1
    # 7. 优化：从大到小累加B/A，直到W，如果B/A大于1，则将B/A设置为1，如果W为奇数，且B/A小于1，则将B/A设置为1，如果W为奇数，且B/A大于1，则将B/A设置为1
    # 8. 优化：从大到小累加B/A，直到W，如果B/A大于1，则将B/A设置为1，如果W为奇数，且B/A小于1，则将B/A设置为1，如果W为奇数，且B/A大于1，则将B/A设置为1，如果W为奇数，且B/A大于1，则将B/A设置为1
    # 9. 优化：从大到小累加B/A，直到W，如果B/A大于1，则将B/A设置为1，如果W为奇数，且B/A小于1，则将B/A设置为1，如果W为
