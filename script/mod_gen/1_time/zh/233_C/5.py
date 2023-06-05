def solve(n, x, bags):
    # 1. 将袋子中的元素分成两组
    # 2. 分别求出两组中的元素的乘积
    # 3. 如果乘积相乘等于x，则结果加1
    # 4. 重复1-3
    # 1. 将袋子中的元素分成两组
    # 2. 分别求出两组中的元素的乘积
    # 3. 如果乘积相乘等于x，则结果加1
    # 4. 重复1-3
    def split_bags(bags):
        if len(bags) == 1:
            return [[], bags]
        if len(bags) == 2:
            return [bags[:1], bags[1:]]
        # 1. 从bags中随机选择一个元素，将其从bags中删除，加入到b1中
        # 2. 将剩余的元素加入到b2中
        # 3. 将b1和b2返回
        import random
        b1 = []
        b2 = []
        while len(bags) > 0:
            idx = random.randint(0, len(bags) - 1)
            b1.append(bags[idx])
            bags.pop(idx)
            if len(bags) > 0:
                idx = random.randint(0, len(bags) - 1)
                b2.append(bags[idx])
                bags.pop(idx)
        return [b1, b2]
    def product(bags):
        import math
        p = 1
        for bag in bags:
            for e in bag:
                p *= e
        return p
    def product2(bags):
        import math
        p = 1
        for e in bags:
            p *= e
        return p
    def find(bags, x, count):
        if len(bags) == 0:
            return count
        if len(bags) == 1:
            if product2(bags[0]) == x:
                return count + 1
            else:
                return count
        if len(bags)

if __name__ == '__main__':
    solve()