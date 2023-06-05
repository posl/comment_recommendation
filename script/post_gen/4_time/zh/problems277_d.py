Synthesizing 9/10 solutions

=======
Suggestion 1

def main():
    n,m = map(int,input().split())
    a = list(map(int,input().split()))

    a.sort()
    s = sum(a)
    ans = s
    for i in range(n):
        if s > 0 and a[i] >= m:
            break
        s -= a[i]
        ans = min(ans,s + (m - a[i]) % m)
    print(ans)

=======
Suggestion 2

def main():
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    a.sort()
    b = [0]*(m+1)
    for i in range(n):
        b[a[i]] += 1
    k = 0
    for i in range(m+1):
        if b[i] > 0:
            k = i
            break
    if k == 0:
        print(0)
        exit()
    c = [0]*(m+1)
    c[0] = b[0]
    for i in range(1,m+1):
        c[i] = c[i-1]+b[i]
    ans = 0
    for i in range(k,m+1):
        ans += c[i]
    print(ans)

=======
Suggestion 3

def main():
    # 读入数据
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    # 答えを格納する変数
    ans = 0
    # 余りを管理する配列
    count = [0] * M
    # 余りごとに数を数える
    for a in A:
        count[a % M] += 1
    # 余りが0のものは一枚だけ使える
    ans += count[0]
    # 余りがM/2のものも一枚だけ使える
    if M % 2 == 0:
        ans += 1
    # それ以外の余りの組み合わせを使う
    for i in range(1, M // 2 + 1):
        # 余りの大きいほうから使っていく
        j = M - i
        # 余りiのカードと余りjのカードを使う
        if count[i] > count[j]:
            ans += count[j]
            count[i] -= count[j]
            count[j] = 0
        else:
            ans += count[i]
            count[j] -= count[i]
            count[i] = 0
    # 余りが0のものが余った場合
    if count[0]:
        ans += count[0] - 1
    # 余りがM/2のものが余った場合
    if M % 2 == 0 and count[M // 2]:
        ans += count[M // 2] - 1
    # それ以外の余りの組み合わせが余った場合
    for i in range(1, M // 2 + 1):
        if count[i]:
            ans += count[i] - 1
    # 答えを出力する
    print(ans)

=======
Suggestion 4

def solve(n, m, a):
    a.sort()
    if a[0] == 0 and a[-1] == m - 1:
        return 0
    if a[0] == 0:
        return m - a[-1] - 1
    if a[-1] == m - 1:
        return a[0] - 1
    ans = 0
    for i in range(1, n):
        if a[i] == a[i - 1]:
            continue
        ans += a[i] - a[i - 1] - 1
    return ans

=======
Suggestion 5

def main():
    # 读入数据
    n, m = map(int, input().split())
    a = list(map(int, input().split()))

    # 统计各个值的个数
    cnt = [0] * m
    for i in range(n):
        cnt[a[i]] += 1

    # 从小到大依次取出
    ans = 0
    for i in range(m):
        # 两个相邻的值之间的差值
        d = cnt[i] - cnt[(i + 1) % m]
        # 如果差值大于0，就从前面的值取出差值个数的牌
        if d > 0:
            ans += d
            cnt[(i + 1) % m] += d
        # 如果差值小于0，就从后面的值取出差值个数的牌
        elif d < 0:
            ans += -d * (m - 1)
            cnt[(i + 1) % m] += d * (m - 1)

    print(ans)

=======
Suggestion 6

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    B = [0] * N
    for i in range(N):
        B[i] = A[i] % M
    B.sort()
    ans = 0
    for i in range(N):
        if i == 0:
            ans += B[i]
        else:
            if B[i] != B[i - 1]:
                ans += B[i]
    print(ans)

=======
Suggestion 7

def main():
    # 读取数据
    N, M = map(int, input().split())
    A = [int(i)%M for i in input().split()]
    # 建立字典，记录每个数字出现的次数
    dic = {}
    for i in A:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
    # 建立一个列表，记录每个数字出现的次数
    B = [0]*M
    for i in dic:
        B[i] = dic[i]
    # 开始计算
    sum = 0
    for i in range(M):
        if B[i] == 0:
            continue
        elif B[i] == 1:
            sum += i
        elif B[i] == 2:
            sum += i
            B[i] = 0
            B[(i+1)%M] += 1
        else:
            sum += (B[i]-2)*i
            B[i] = 2
            B[(i+1)%M] += 1
            B[(i+2)%M] += 1
    print(sum)

=======
Suggestion 8

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    #print(a)
    #print(n, m)
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
    #print(a

=======
Suggestion 9

def main():
    N,M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    A = [a%M for a in A]
    #print(A)
    #print(M)
    #print(N)
    #print(A[0])
    #print(A[1])
    #print(A[2])
    #print(A[3])
    #print(A[4])
    #print(A[5])
    #print(A[6])
    #print(A[7])
    #print(A[8])
    #print(A[9])
    #print(A[10])
    #print(A[11])
    #print(A[12])
    #print(A[13])
    #print(A[14])
    #print(A[15])
    #print(A[16])
    #print(A[17])
    #print(A[18])
    #print(A[19])
    #print(A[20])
    #print(A[21])
    #print(A[22])
    #print(A[23])
    #print(A[24])
    #print(A[25])
    #print(A[26])
    #print(A[27])
    #print(A[28])
    #print(A[29])
    #print(A[30])
    #print(A[31])
    #print(A[32])
    #print(A[33])
    #print(A[34])
    #print(A[35])
    #print(A[36])
    #print(A[37])
    #print(A[38])
    #print(A[39])
    #print(A[40])
    #print(A[41])
    #print(A[42])
    #print(A[43])
    #print(A[44])
    #print(A[45])
    #print(A[46])
    #print(A[47])
    #print(A[48])
    #print(A[49])
    #print(A[50])
    #print(A[51])
    #print(A[52])
    #print(A[53])
    #print(A[54])
    #print(A[55])
    #print(A[56])
    #print(A[57])
    #print(A[58])
    #print(A[59])
    #print(A[60])
    #print(A[61])
    #print(A[62])
    #print(A[
