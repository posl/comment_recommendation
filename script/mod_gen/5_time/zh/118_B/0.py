def main():
    # 读取数据
    n, m = map(int, input().split())
    like = [set(map(int, input().split()[1:])) for _ in range(n)]
    # 判断
    ans = set(range(1, m + 1))
    for i in like:
        ans &= i
    # 输出
    print(len(ans))

if __name__ == '__main__':
    main()