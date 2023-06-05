def jump(N, X, a, b):
    # 从第N个开始跳，看是否能跳到X
    if N == 0:
        return False
    if X == a[N - 1] or X == b[N - 1]:
        return True
    if X < a[N - 1]:
        return False
    if X > b[N - 1]:
        return False
    return jump(N - 1, X - a[N - 1], a, b) or jump(N - 1, X - b[N - 1], a, b)

if __name__ == '__main__':
    jump()