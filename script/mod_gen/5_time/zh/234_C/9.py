def find(k):
    # 用队列来存储
    queue = []
    # 从1开始
    queue.append(1)
    # 计数器
    count = 0
    # 循环
    while True:
        # 弹出队列中的第一个元素
        num = queue.pop(0)
        # 计数器加1
        count += 1
        # 检查计数器是否与k相等
        if count == k:
            # 相等则返回
            return num
        # 检查num是否可以被10整除
        if num % 10 == 0:
            # 可以则将num乘以10加1
            queue.append(num * 10 + 1)
        # 将num乘以10加2
        queue.append(num * 10 + 2)

if __name__ == '__main__':
    find()