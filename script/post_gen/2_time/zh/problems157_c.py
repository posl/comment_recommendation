Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, M = map(int, input().split())
    s = []
    c = []
    for i in range(M):
        s_i, c_i = map(int, input().split())
        s.append(s_i)
        c.append(c_i)
    #print(N, M, s, c)
    num = []
    for i in range(N):
        num.append(-1)
    for i in range(M):
        num[s[i]-1] = c[i]
    #print(num)
    if num[0] == 0 and N != 1:
        print(-1)
    else:
        for i in range(N):
            if num[i] == -1:
                num[i] = 0
        #print(num)
        ans = 0
        for i in range(N):
            ans += num[i] * (10**(N-i-1))
        print(ans)

=======
Suggestion 2

def main():
    N, M = map(int, input().split())
    s = []
    c = []
    for i in range(M):
        a, b = map(int, input().split())
        s.append(a)
        c.append(b)
    if N == 1 and M == 0:
        print(0)
    elif N == 1 and M == 1:
        print(c[0])
    elif N == 1 and M > 1:
        print(-1)
    elif N == 2 and M == 0:
        print(10)
    elif N == 2 and M == 1:
        print(-1)
    elif N == 2 and M == 2:
        if s[0] == 1 and s[1] == 2:
            print(c[0]*10+c[1])
        elif s[0] == 2 and s[1] == 1:
            print(c[1]*10+c[0])
        else:
            print(-1)
    elif N == 2 and M > 2:
        print(-1)
    elif N == 3 and M == 0:
        print(100)
    elif N == 3 and M == 1:
        print(-1)
    elif N == 3 and M == 2:
        if s[0] == 1 and s[1] == 2:
            print(c[0]*100+c[1]*10)
        elif s[0] == 1 and s[1] == 3:
            print(c[0]*100+c[1])
        elif s[0] == 2 and s[1] == 1:
            print(c[1]*100+c[0]*10)
        elif s[0] == 2 and s[1] == 3:
            print(c[1]*100+c[0])
        elif s[0] == 3 and s[1] == 1:
            print(c[1]*100+c[0])
        elif s[0] == 3 and s[1] == 2:
            print(c[1]*100+c[0]*10)
        else:
            print(-1)
    elif N == 3 and M == 3:
        if s[0] == 1 and s[1] == 2 and s[2]

=======
Suggestion 3

def solve(N, M, s, c):
    #N: 位数
    #M: 条件数
    #s: 条件位置
    #c: 条件值
    #print(N, M, s, c)
    if N == 1:
        if M == 0:
            return 0
        elif M == 1:
            return c[0]
        else:
            return -1
    elif N == 2:
        if M == 0:
            return 0
        elif M == 1:
            if s[0] == 1:
                return c[0] * 10
            else:
                return c[0] + 10
        elif M == 2:
            if s[0] == 1:
                return c[0] * 10 + c[1]
            elif s[0] == 2:
                return c[1] * 10 + c[0]
            else:
                return -1
        else:
            return -1
    else:
        if M == 0:
            return 0
        elif M == 1:
            if s[0] == 1:
                return c[0] * 100
            elif s[0] == 2:
                return c[0] * 10
            else:
                return c[0]
        elif M == 2:
            if s[0] == 1 and s[1] == 2:
                return c[0] * 100 + c[1] * 10
            elif s[0] == 1 and s[1] == 3:
                return c[0] * 100 + c[1]
            elif s[0] == 2 and s[1] == 1:
                return c[1] * 100 + c[0] * 10
            elif s[0] == 2 and s[1] == 3:
                return c[1] * 10 + c[0]
            elif s[0] == 3 and s[1] == 1:
                return c[1] * 100 + c[0]
            elif s[0] == 3 and s[1] == 2:
                return c[1] * 10 + c

=======
Suggestion 4

def main():
    while True:
        try:
            N, M = map(int, input().split())
            if N < 1 or N > 3 or M < 0 or M > 5:
                print(-1)
                continue
            num = [0] * N
            for i in range(M):
                s, c = map(int, input().split())
                if s < 1 or s > N or c < 0 or c > 9:
                    print(-1)
                    break
                num[s - 1] = c
            else:
                if N == 1:
                    if num[0] == 0:
                        print(0)
                    else:
                        print(num[0])
                elif N == 2:
                    if num[0] == 0:
                        print(-1)
                    else:
                        print(num[0] * 10 + num[1])
                elif N == 3:
                    if num[0] == 0 and num[1] == 0:
                        print(-1)
                    elif num[0] == 0 and num[1] != 0:
                        print(num[1] * 10 + num[2])
                    elif num[0] != 0 and num[1] == 0:
                        print(num[0] * 100 + num[2])
                    else:
                        print(num[0] * 100 + num[1] * 10 + num[2])
        except:
            break

=======
Suggestion 5

def main():
    N,M = map(int,input().split())
    s = []
    c = []
    for i in range(0,M):
        s1,c1 = map(int,input().split())
        s.append(s1)
        c.append(c1)
    s_c = list(zip(s,c))
    s_c.sort()
    s,c = zip(*s_c)
    if N == 1:
        if M == 0:
            print(0)
        elif M == 1:
            print(c[0])
        else:
            print(-1)
    elif N == 2:
        if M == 0:
            print(0)
        elif M == 1:
            if s[0] == 1:
                print(c[0])
            elif s[0] == 2:
                print(c[0]*10)
            else:
                print(-1)
        elif M == 2:
            if s[0] == 1 and s[1] == 2:
                print(c[0]*10+c[1])
            elif s[0] == 2 and s[1] == 1:
                print(c[1]*10+c[0])
            else:
                print(-1)
        else:
            print(-1)
    elif N == 3:
        if M == 0:
            print(0)
        elif M == 1:
            if s[0] == 1:
                print(c[0])
            elif s[0] == 2:
                print(c[0]*10)
            elif s[0] == 3:
                print(c[0]*100)
            else:
                print(-1)
        elif M == 2:
            if s[0] == 1 and s[1] == 2:
                print(c[0]*10+c[1])
            elif s[0] == 2 and s[1] == 3:
                print(c[0]*10+c[1])
            elif s[0] == 3 and s[1] == 1:
                print(c[1]*100+c[0])
            elif s[0] == 1 and s[1] == 3:
                print(c[0]*100+c[1])
            elif s[0] == 2 and s[1] == 1:
                print(c[1]*10+c

=======
Suggestion 6

def solve():
    N,M = map(int,input().split())
    s = [0]*M
    c = [0]*M
    for i in range(M):
        s[i],c[i] = map(int,input().split())
    #print(s,c)
    ans = -1
    for i in range(10**N):
        num = str(i).zfill(N)
        flag = True
        for j in range(M):
            if num[s[j]-1] != str(c[j]):
                flag = False
                break
        if flag:
            ans = i
            break
    print(ans)
    return 0

=======
Suggestion 7

def get_input():
    # N M
    # s_1 c_1
    # .
    # .
    # .
    # s_M c_M
    N, M = map(int, input().split())
    s_c = []
    for i in range(M):
        s_c.append(list(map(int, input().split())))
    return N, M, s_c

=======
Suggestion 8

def main():
    # 输入
    N, M = map(int, input().split())
    s_c = [list(map(int, input().split())) for _ in range(M)]

    # 处理
    # 1. 生成一个列表，用于存储最终结果
    result = [0 for _ in range(N)]
    # 2. 遍历输入的数据
    for s, c in s_c:
        # 2.1 如果输入的位置是第一位，且输入的数字是0，那么直接返回-1
        if s == 1 and c == 0:
            print(-1)
            return
        # 2.2 如果输入的位置不是第一位，且输入的数字是0，那么直接将该位置的数字设置为0
        if s != 1 and c == 0:
            result[s-1] = 0
        # 2.3 如果输入的位置是第一位，且输入的数字不是0，那么直接将该位置的数字设置为输入的数字
        if s == 1 and c != 0:
            result[s-1] = c
        # 2.4 如果输入的位置不是第一位，且输入的数字不是0，那么直接将该位置的数字设置为输入的数字
        if s != 1 and c != 0:
            result[s-1] = c
    # 3. 如果第一位是0，那么直接返回-1
    if result[0] == 0:
        print(-1)
        return
    # 4. 将列表转换成字符串，然后转换成整数
    result = int("".join(map(str, result)))
    # 5. 打印结果
    print(result)

=======
Suggestion 9

def main():
    N,M = map(int,input().split())
    s = []
    c = []
    for i in range(M):
        s1,c1 = map(int,input().split())
        s.append(s1)
        c.append(c1)
    for i in range(10**(N-1),10**N):
        s_i = str(i)
        flag = True
        for j in range(M):
            if int(s_i[s[j]-1]) != c[j]:
                flag = False
                break
        if flag:
            print(i)
            break
    else:
        print(-1)

=======
Suggestion 10

def main():
    n, m = map(int, input().split())
    s = []
    c = []
    for i in range(m):
        s_i, c_i = map(int, input().split())
        s.append(s_i)
        c.append(c_i)
    for i in range(10**(n-1), 10**n):
        for j in range(m):
            if int(str(i)[s[j]-1]) != c[j]:
                break
        else:
            print(i)
            break
    else:
        print(-1)
