def main():
    # 读入数据
    N, M = map(int, input().split())
    A = [list(map(int, input().split()))[1:] for _ in range(N)]
    # 枚举所有食物
    ans = 0
    for i in range(1, M + 1):
        # 判断是否所有人都喜欢食物 i
        for a in A:
            if i not in a:
                break
        else:
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()