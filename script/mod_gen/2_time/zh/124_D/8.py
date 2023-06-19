def main():
    # 读入数据
    n, k = map(int, input().split())
    s = input()
    # 从左到右，将连续的0或1的数量记录到列表中
    cnt = []
    now = s[0]
    num = 1
    for i in range(1, n):
        if s[i] == now:
            num += 1
        else:
            cnt.append(num)
            now = s[i]
            num = 1
    cnt.append(num)
    # 从左到右，将连续的0或1的数量记录到列表中
    cnt = []
    now = s[0]
    num = 1
    for i in range(1, n):
        if s[i] == now:
            num += 1
        else:
            cnt.append(num)
            now = s[i]
            num = 1
    cnt.append(num)
    # 如果第一个是0，那么第一个0之前和最后一个0之后的1都可以被翻转
    if s[0] == "0":
        ans = sum(cnt[:2 * k + 1])
    # 如果第一个是1，那么第一个1之前和最后一个1之后的0都可以被翻转
    else:
        ans = sum(cnt[:2 * k + 2])
    # 从第二个开始，每两个数之间的间隔都可以被翻转
    for i in range(1, len(cnt) - 2 * k):
        ans = max(ans, sum(cnt[i:i + 2 * k + 1]))
    # 如果最后一个是0，那么最后一个0之前和最后一个0之后的1都可以被翻转
    if s[-1] == "0":
        ans = max(ans, sum(cnt[-2 * k - 1:]))
    # 如果最后一个是1，那么最后一个1之前和最后一个1之后的0都可以被翻转
    else:
        ans = max(ans, sum(cnt[-2 * k - 2:]))
    print(ans)

if __name__ == '__main__':
    main()