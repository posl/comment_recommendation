def cal(n, a, b):
    total = 0
    for i in range(n):
        total += a[i] / b[i]
    half = total / 2
    total = 0
    for i in range(n):
        total += a[i] / b[i]
        if total >= half:
            return i + 1 - (total - half) * b[i] / a[i]
    return -1

if __name__ == '__main__':
    cal()