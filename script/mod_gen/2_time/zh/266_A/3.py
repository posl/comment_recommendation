def problems265_d():
    N, P, Q, R = map(int, input().split())
    A = list(map(int, input().split()))
    # print(N, P, Q, R)
    # print(A)
    if N < 4:
        print('No')
        return
    # 从左边开始，找到第一个满足条件的x
    # 从右边开始，找到第一个满足条件的w
    # 从x到y，求和，判断是否为P
    # 从y到z，求和，判断是否为Q
    # 从z到w，求和，判断是否为R
    # 如果都满足，则输出Yes，否则输出No
    # 从左边开始，找到第一个满足条件的x
    x = 0
    while x < N - 3:
        sum = A[x]
        if sum == P:
            break
        x += 1
    if x == N - 3:
        print('No')
        return
    # 从右边开始，找到第一个满足条件的w
    w = N - 1
    while w > x + 2:
        sum = A[w]
        if sum == R:
            break
        w -= 1
    if w == x + 2:
        print('No')
        return
    # 从x到y，求和，判断是否为P
    y = x + 1
    sum = A[x]
    while y < w:
        sum += A[y]
        if sum == P:
            break
        y += 1
    if y == w:
        print('No')
        return
    # 从y到z，求和，判断是否为Q
    z = y + 1
    sum = A[y]
    while z < w:
        sum += A[z]
        if sum == Q:
            break
        z += 1
    if z == w:
        print('No')
        return
    # 从z到w，求和，判断是否为R
    sum = A[z]
    while z < w:
        sum += A[z

if __name__ == '__main__':
    problems265_d()