def main():
    # 读入数据
    n, k = map(int, input().split())
    s = []
    for i in range(n):
        s.append(input())
    # 递归求解
    print(solve(s, k))
