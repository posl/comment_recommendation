def solve():
    # 读入数据
    n, q = map(int, input().split())
    s = input()
    query = [list(map(int, input().split())) for _ in range(q)]
    # 处理
    # 1.找到第一个被移动的字符位置
    # 2.找到该字符被移动后的位置
    # 3.根据移动的次数和字符移动后的位置，计算出字符移动后的位置
    # 4.根据移动后的位置，找到原来的字符
    # 5.输出
    # 6.重复1-5
    for t, x in query:
        x = x - 1
        for _ in range(x):
            if s[x] == s[x - 1]:
                x -= 1
            else:
                break
        x = (x - t) % n
        print(s[x])

if __name__ == '__main__':
    solve()