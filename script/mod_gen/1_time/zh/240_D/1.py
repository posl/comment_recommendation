def main():
    #读取输入
    n = int(input())
    a = list(map(int, input().split()))
    #按照题意，从后往前遍历
    #遍历时，每次判断当前数和前一个数是否相等
    #如果相等，就将当前数和前一个数都删除
    #如果不相等，就将当前数放入列表中
    #最后，输出列表的长度
    ans = []
    for i in range(n-1, -1, -1):
        if i == n-1:
            ans.append(a[i])
        elif a[i] == a[i+1]:
            ans.pop()
        else:
            ans.append(a[i])
    #从后往前输出
    for i in range(len(ans)-1, -1, -1):
        print(ans[i])

if __name__ == '__main__':
    main()