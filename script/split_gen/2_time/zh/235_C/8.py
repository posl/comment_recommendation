def main():
    n = int(input())
    h = list(map(int, input().split()))
    # 从左边开始，找到最大的那个，然后从右边开始，找到最大的那个，然后比较两个最大的那个，取最大的那个
    # 从左边开始，找到最大的那个
    max_left = 0
    for i in range(n):
        if h[i] > max_left:
            max_left = h[i]
    # 从右边开始，找到最大的那个
    max_right = 0
    for i in range(n-1, -1, -1):
        if h[i] > max_right:
            max_right = h[i]
    # 比较两个最大的那个，取最大的那个
    if max_right > max_left:
        print(max_right)
    else:
        print(max_left)
