def main():
    n, q = map(int, input().split())
    s = input()
    # 1. 生成累积和列表
    acc = [0]
    for i in range(1, n):
        if s[i - 1] == 'A' and s[i] == 'C':
            acc.append(acc[i - 1] + 1)
        else:
            acc.append(acc[i - 1])
    # 2. 解决每个查询
    for _ in range(q):
        l, r = map(int, input().split())
        print(acc[r - 1] - acc[l - 1])

if __name__ == '__main__':
    main()