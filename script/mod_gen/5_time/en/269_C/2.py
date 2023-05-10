def check(x, n):
    while x > 0:
        if x & 1:
            if n & 1 == 0:
                return False
        x >>= 1
        n >>= 1
    return True
n = int(input())
for i in range(1 << 15):
    x = 0
    for j in range(15):
        if i & (1 << j):
            x += 1 << j
    if x <= n and check(x, n):
        print(x)

if __name__ == '__main__':
    check()