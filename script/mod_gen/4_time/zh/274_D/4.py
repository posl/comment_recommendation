def solve(N, x, y, A):
    # 1. x, y 与 A 中所有元素的和的奇偶性必须一致
    if (x + y) % 2 != sum(A) % 2:
        return False
    # 2. x, y 与 A 中所有元素的绝对值的最大值必须小于等于 A 中所有元素的和
    if max(abs(x), abs(y)) > sum(A):
        return False
    # 3. x, y 与 A 中所有元素的和的绝对值必须小于等于 A 中所有元素的最大值
    if abs(x + y) > max(A):
        return False
    return True

if __name__ == '__main__':
    solve()