def main():
    n = int(input())
    s = []
    for _ in range(n):
        s.append(input())
    # 从后往前推导
    # 1.最后一位必须是True
    # 2.前一位的值必须和s[i]的值相等
    # 3.如果s[i]是AND，前一位的值必须是True
    # 4.如果s[i]是OR，前一位的值必须是False
    ans = 1
    for i in range(n-1, -1, -1):
        if s[i] == "AND":
            ans = ans * 2 + 1
        else:
            ans = ans * 2
    print(ans)

if __name__ == '__main__':
    main()