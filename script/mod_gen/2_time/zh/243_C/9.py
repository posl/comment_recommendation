def main():
    n = int(input())
    xy = [tuple(map(int,input().split())) for i in range(n)]
    s = input()
    # 向右走的人
    r = [xy[i] for i in range(n) if s[i] == 'R']
    # 向左走的人
    l = [xy[i] for i in range(n) if s[i] == 'L']
    # 按照x坐标排序
    r.sort()
    l.sort()
    # 从左到右遍历向右走的人
    for i in range(len(r)):
        # 从右到左遍历向左走的人
        for j in range(len(l) - 1, -1, -1):
            # 如果向右走的人的x坐标大于向左走的人的x坐标
            if r[i][0] > l[j][0]:
                # 如果向右走的人的y坐标大于向左走的人的y坐标
                if r[i][1] > l[j][1]:
                    # 如果向左走的人的下一个人的x坐标大于向右走的人的下一个人的x坐标
                    if l[j + 1][0] > r[i + 1][0]:
                        # 如果向左走的人的下一个人的y坐标大于向右走的人的下一个人的y坐标
                        if l[j + 1][1] > r[i + 1][1]:
                            print('Yes')
                            return
                else:
                    # 如果向左走的人的下一个人的x坐标大于向右走的人的下一个人的x坐标
                    if l[j + 1][0] > r[i + 1][0]:
                        # 如果向左走的人的下一个人的y坐标大于向右走的人的下一个人的y坐标
                        if l[j + 1][1] > r[i + 1][1]:
                            print('Yes')
                            return
    print('No')
if

if __name__ == '__main__':
    main()