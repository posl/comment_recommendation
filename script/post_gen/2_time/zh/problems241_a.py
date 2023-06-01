Synthesizing 10/10 solutions

=======
Suggestion 1

def input():
    n = int(input())
    a = list(map(int, input().split()))
    return n, a

=======
Suggestion 2

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

=======
Suggestion 3

def main():
    N = int(input())
    a = list(map(int, input().split()))
    l = [0] * (2 * 10 ** 5 + 1)
    for i in range(N):
        l[a[i]] += 1
    ans = 0
    for i in range(2 * 10 ** 5 + 1):
        if l[i] > 0:
            ans += 1
    print(ans)

=======
Suggestion 4

def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = [0] * n
    count = {}
    for i in range(n):
        x = a[i]
        if x in count:
            count[x] += 1
        else:
            count[x] = 1
        if count[x] == x:
            ans[i] = 1
        else:
            ans[i] = 0
    for i in range(n):
        print(ans[i])

=======
Suggestion 5

def main():
    n = int(input())
    a = list(map(int,input().split()))
    # print(n)
    # print(a)

    # print(a)
    # print(a[0])
    # print(a[1])
    # print(a[2])
    # print(a[3])

    # print(a[0:2])
    # print(a[1:3])
    # print(a[2:4])
    # print(a[3:5])

    # print(a[0:3])
    # print(a[1:4])
    # print(a[2:5])
    # print(a[3:6])

    # print(a[0:4])
    # print(a[1:5])
    # print(a[2:6])
    # print(a[3:7])

    # print(a[0:5])
    # print(a[1:6])
    # print(a[2:7])
    # print(a[3:8])

    # print(a[0:6])
    # print(a[1:7])
    # print(a[2:8])
    # print(a[3:9])

    # print(a[0:7])
    # print(a[1:8])
    # print(a[2:9])
    # print(a[3:10])

    # print(a[0:8])
    # print(a[1:9])
    # print(a[2:10])

    # print(a[0:9])
    # print(a[1:10])

    # print(a[0:10])

    # print(a[0:1])
    # print(a[1:2])
    # print(a[2:3])
    # print(a[3:4])
    # print(a[4:5])
    # print(a[5:6])
    # print(a[6:7])
    # print(a[7:8])
    # print(a[8:9])
    # print(a[9:10])

    # print(a[0:2])
    # print(a[1:3])
    # print(a[2:4])
    # print(a[3:5])
    # print(a[4:6])
    # print(a[5:7])
    # print(a[6:8])
    # print(a[7:9])
    # print(a[8:

=======
Suggestion 6

def main():
    N = int(input())
    a = list(map(int, input().split()))
    #print(N)
    #print(a)
    #print(len(a))
    #print(a[0])
    #print(a[1])
    #print(a[2])
    #print(a[3])
    #print(a[4])
    #print(a[5])
    #print(a[6])
    #print(a[7])
    #print(a[8])
    #print(a[9])
    #print(a[10])
    #print(a[11])
    #print(a[12])
    #print(a[13])
    #print(a[14])
    #print(a[15])
    #print(a[16])
    #print(a[17])
    #print(a[18])
    #print(a[19])
    #print(a[20])
    #print(a[21])
    #print(a[22])
    #print(a[23])
    #print(a[24])
    #print(a[25])
    #print(a[26])
    #print(a[27])
    #print(a[28])
    #print(a[29])
    #print(a[30])
    #print(a[31])
    #print(a[32])
    #print(a[33])
    #print(a[34])
    #print(a[35])
    #print(a[36])
    #print(a[37])
    #print(a[38])
    #print(a[39])
    #print(a[40])
    #print(a[41])
    #print(a[42])
    #print(a[43])
    #print(a[44])
    #print(a[45])
    #print(a[46])
    #print(a[47])
    #print(a[48])
    #print(a[49])
    #print(a[50])
    #print(a[51])
    #print(a[52])
    #print(a[53])
    #print(a[54])
    #print(a[55])
    #print(a[56])
    #print(a[57])
    #print(a[58])
    #print(a[59])
    #print(a[60])
    #print(a[61])
    #print(a[62])
    #print(a[63])
    #print(a[64])
    #print(a[65])
    #print

=======
Suggestion 7

def main():
    n = int(input())
    a = list(map(int, input().split()))

    a.sort()
    a.append(0)
    ans = 0
    cnt = 1
    for i in range(n):
        if a[i] != a[i+1]:
            if cnt >= a[i]:
                ans += cnt - a[i]
            else:
                ans += cnt
            cnt = 1
        else:
            cnt += 1

    print(ans)

=======
Suggestion 8

def main():
    # 读入数据
    n = int(input())
    a = list(map(int, input().split()))
    # 各个数字的数量
    count = {}
    for i in a:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
    # 每个数字的最大长度
    length = {}
    for i in count:
        length[i] = 1
    # 从小到大遍历
    for i in range(2, max(a) + 1):
        if i in count:
            # 如果有i的数字
            # 从小到大遍历i的倍数，更新最大长度
            for j in range(2 * i, max(a) + 1, i):
                if j in length and length[j] < length[i] + 1:
                    length[j] = length[i] + 1
    # 输出
    for i in a:
        print(n - length[i] + 1)

=======
Suggestion 9

def main():
    n = int(input())
    a = list(map(int, input().split()))
    dict = {}
    for i in range(n):
        if a[i] not in dict:
            dict[a[i]] = 1
        else:
            dict[a[i]] += 1
    ans = 0
    for k in dict:
        if dict[k] >= k:
            ans += dict[k] - k
        else:
            ans += dict[k]
    print(ans)

=======
Suggestion 10

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = [0] * (2 * 10 ** 5 + 1)
    ans = [0] * n
    for i in range(n):
        b[a[i]] += 1
    for i in range(2 * 10 ** 5, 1, -1):
        if b[i] == 0:
            continue
        if b[i] == 1:
            ans[0] += 1
        else:
            ans[0] += 1
            ans[b[i]] -= 1
            ans[b[i] + 1] += 1
    for i in range(1, n):
        ans[i] += ans[i - 1]
    print('\n'.join(map(str, ans)))

main()
