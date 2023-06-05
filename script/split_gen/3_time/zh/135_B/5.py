def main():
    N = int(input())
    p = list(map(int, input().split()))
    # 1. 降序排序
    # 2. 降序排序后的序列 p 与原序列 p 比较，如果相同则输出 YES，否则输出 NO
    # 3. 降序排序后的序列 p 与原序列 p 比较，如果相同则输出 YES，否则输出 NO
    # 4. 降序排序后的序列 p 与原序列 p 比较，如果相同则输出 YES，否则输出 NO
    # 5. 降序排序后的序列 p 与原序列 p 比较，如果相同则输出 YES，否则输出 NO
    # 6. 降序排序后的序列 p 与原序列 p 比较，如果相同则输出 YES，否则输出 NO
    # 7. 降序排序后的序列 p 与原序列 p 比较，如果相同则输出 YES，否则输出 NO
    # 8. 降序排序后的序列 p 与原序列 p 比较，如果相同则输出 YES，否则输出 NO
    # 9. 降序排序后的序列 p 与原序列 p 比较，如果相同则输出 YES，否则输出 NO
    # 10. 降序排序后的序列 p 与原序列 p 比较，如果相同则输出 YES，否则输出 NO
    # 降序排序
    p.sort(reverse=True)
    # 降序排序后的序列 p 与原序列 p 比较，如果相同则输出 YES，否则输出 NO
    if p == list(range(1, N + 1)):
        print('YES')
    else:
        print('NO')
