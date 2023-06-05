def main():
    # 读取输入
    n = int(input())
    x, y = map(int, input().split())
    a = []
    b = []
    for i in range(n):
        a_i, b_i = map(int, input().split())
        a.append(a_i)
        b.append(b_i)
    # 处理
    # 1. 如果x，y都大于a，b的和，那么肯定是-1
    if x > sum(a) or y > sum(b):
        print(-1)
        return
    # 2. 如果x，y都小于a，b的最小值，那么肯定是-1
    if x < min(a) or y < min(b):
        print(-1)
        return
    # 3. 如果x，y都等于a，b的最小值，那么肯定是1
    if x == min(a) and y == min(b):
        print(1)
        return
    # 4. 如果x，y都等于a，b的和，那么肯定是n
    if x == sum(a) and y == sum(b):
        print(n)
        return
    # 5. 如果x，y都等于a，b的最大值，那么肯定是n
    if x == max(a) and y == max(b):
        print(n)
        return
    # 6. 如果x，y都等于a，b的最大值，那么肯定是n
    if x == max(a) and y == max(b):
        print(n)
        return
    # 7. 如果x，y都等于a，b的最大值，那么肯定是n
    if x == max(a) and y == max(b):
        print(n)
        return
    # 8. 如果x，y都等于a，b的最大值，那么肯定是n
    if x == max(a) and y == max(b):
        print(n)
        return
    # 9. 如果x，y都等于a，b的最大值，那么肯定是n
    if x ==

if __name__ == '__main__':
    main()