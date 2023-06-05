def main():
    n = int(input())
    h = list(map(int, input().split()))
    # 从左向右遍历，如果后一个比前一个大，那么就上去
    # 如果后一个比前一个小，那么就停止
    # 一直到最后一个
    # 所以就是找到最大的那个
    max_h = 0
    for i in range(n):
        if max_h < h[i]:
            max_h = h[i]
    print(max_h)

if __name__ == '__main__':
    main()