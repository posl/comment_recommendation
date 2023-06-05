Synthesizing 9/10 solutions

=======
Suggestion 1

def main():
    n,m = map(int,input().split())
    s_c = []
    for i in range(m):
        s_c.append(list(map(int,input().split())))
    s_c.sort()
    num = 0
    for i in range(m):
        num += s_c[i][1] * 10 ** (n - s_c[i][0])
    if len(str(num)) == n:
        print(num)
    else:
        print(-1)

=======
Suggestion 2

def main():
    n, m = map(int, input().split())
    sc = [list(map(int, input().split())) for _ in range(m)]
    ans = -1
    for i in range(10 ** n):
        i = str(i)
        if len(i) == n:
            for s, c in sc:
                if i[s - 1] != str(c):
                    break
            else:
                ans = i
                break
    print(ans)

=======
Suggestion 3

def main():
    N, M = map(int, input().split())
    #print(N, M)
    #print(type(N), type(M))
    s = []
    c = []
    for i in range(M):
        s_i, c_i = map(int, input().split())
        s.append(s_i)
        c.append(c_i)
    #print(s, c)
    #print(type(s), type(c))
    #print(len(s), len(c))
    #print(type(s[0]), type(c[0]))
    #print(type(s[1]), type(c[1]))
    #print(type(s[2]), type(c[2]))
    #print(type(s[3]), type(c[3]))
    #print(type(s[4]), type(c[4]))
    #print(type(s[5]), type(c[5]))
    #print(type(s[6]), type(c[6]))
    #print(type(s[7]), type(c[7]))
    #print(type(s[8]), type(c[8]))
    #print(type(s[9]), type(c[9]))
    #print(type(s[10]), type(c[10]))
    #print(type(s[11]), type(c[11]))
    #print(type(s[12]), type(c[12]))
    #print(type(s[13]), type(c[13]))
    #print(type(s[14]), type(c[14]))
    #print(type(s[15]), type(c[15]))
    #print(type(s[16]), type(c[16]))
    #print(type(s[17]), type(c[17]))
    #print(type(s[18]), type(c[18]))
    #print(type(s[19]), type(c[19]))
    #print(type(s[20]), type(c[20]))
    #print(type(s[21]), type(c[21]))
    #print(type(s[22]), type(c[22]))
    #print(type(s[23]), type(c[23]))
    #print(type(s[24]), type(c[24]))
    #print(type(s[25]), type(c[25]))
    #print(type(s[26]), type(c[26]))
    #print(type(s[27]), type(c[27]))
    #print(type(s[28]), type(c[28]))
    #print(type(s[29]), type(c[29]))
    #print(type(s[30]), type(c[30]))

=======
Suggestion 4

def main():
    # 读取数据
    N, M = map(int, input().split())
    s_c = []
    for i in range(M):
        s_c.append(list(map(int, input().split())))
    # 从小到大排序
    s_c.sort()

    # 从最大的数开始，逐个减1，直到满足条件
    num = ''
    for i in range(10 ** N - 1, -1, -1):
        num = str(i)
        flag = True
        for j in range(M):
            if num[s_c[j][0] - 1] != str(s_c[j][1]):
                flag = False
                break
        if flag:
            break

    # 输出结果
    if flag:
        print(num)
    else:
        print(-1)

=======
Suggestion 5

def main():
    N, M = map(int, input().split())
    s = []
    c = []
    for i in range(M):
        s_i, c_i = map(int, input().split())
        s.append(s_i)
        c.append(c_i)
    if N == 1:
        if M == 1:
            print(c[0])
        else:
            print(-1)
    elif N == 2:
        if M == 1:
            if s[0] == 1:
                print(c[0] * 10)
            else:
                print(c[0])
        elif M == 2:
            if s[0] == 1:
                print(c[0] * 10 + c[1])
            elif s[0] == 2:
                print(c[1] * 10 + c[0])
            else:
                print(-1)
        else:
            print(-1)
    else:
        if M == 1:
            if s[0] == 1:
                print(c[0] * 100)
            elif s[0] == 2:
                print(c[0] * 10)
            elif s[0] == 3:
                print(c[0])
            else:
                print(-1)
        elif M == 2:
            if s[0] == 1:
                if s[1] == 2:
                    print(c[0] * 100 + c[1] * 10)
                elif s[1] == 3:
                    print(c[0] * 100 + c[1])
                else:
                    print(-1)
            elif s[0] == 2:
                if s[1] == 1:
                    print(c[1] * 100 + c[0] * 10)
                elif s[1] == 3:
                    print(c[1] * 10 + c[0])
                else:
                    print(-1)
            elif s[0] == 3:
                if s[1] == 1:
                    print(c[1] * 100 + c[0])
                elif s[1] == 2:
                    print(c[1] * 10 + c[0])
                else:
                    print(-1)
            else:
                print(-1)
        elif M == 3:

=======
Suggestion 6

def solve(N, M, s, c):
    if N == 1:
        return c[0]
    elif N == 2:
        if s[0] == 1 and c[0] == 0:
            return -1
        else:
            return c[0] * 10 + c[1]
    elif N == 3:
        if s[0] == 1 and c[0] == 0:
            return -1
        elif s[1] == 2 and c[1] == 0:
            return -1
        else:
            return c[0] * 100 + c[1] * 10 + c[2]
    else:
        return -1

=======
Suggestion 7

def f(n,m):
    if n==1:
        return 0
    elif n==2:
        return 10
    elif n==3:
        return 100
    else:
        return -1

=======
Suggestion 8

def main():
    N, M = map(int, input().split())
    s = []
    c = []
    for i in range(M):
        s_i, c_i = map(int, input().split())
        s.append(s_i)
        c.append(c_i)

    #print(N, M, s, c)
    #print(len(s), len(c))

    #print(s.index(1))
    #print(c[s.index(1)])

    if N == 1:
        if M == 0:
            print(0)
        elif M == 1:
            print(c[0])
        else:
            print(-1)
    elif N == 2:
        if M == 0:
            print(10)
        elif M == 1:
            print(10+c[0])
        elif M == 2:
            print(c[0]*10+c[1])
        else:
            print(-1)
    elif N == 3:
        if M == 0:
            print(100)
        elif M == 1:
            print(100+c[0]*10)
        elif M == 2:
            print(100+c[0]*10+c[1])
        elif M == 3:
            print(c[0]*100+c[1]*10+c[2])
        else:
            print(-1)
    else:
        print(-1)

=======
Suggestion 9

def get_number(n, m, s, c):
    #n 位数，m 个条件
    #s_i 位置，c_i 数字
    #1. 从左到右，每个位置都有可能的数字
    #2. 从左到右，每个位置都有可能的数字，但是如果有条件，那么就只能是条件的数字
    #3. 从左到右，每个位置都有可能的数字，但是如果有条件，那么就只能是条件的数字，如果有多个，那么就取最小的那个
    #4. 从左到右，每个位置都有可能的数字，但是如果有条件，那么就只能是条件的数字，如果有多个，那么就取最小的那个，如果这个数字是0，那么就不行
    #5. 从左到右，每个位置都有可能的数字，但是如果有条件，那么就只能是条件的数字，如果有多个，那么就取最小的那个，如果这个数字是0，那么就不行，如果这个数字是第一位，那么就不行
    #6. 从左到右，每个位置都有可能的数字，但是如果有条件，那么就只能是条件的数字，如果有多个，那么就取最小的那个，如果这个数字是0，那么就不行，如果这个数字是第一位，那么就不行，如果这个数字是第一位，且是0，那么就不行
    #7. 从左到右，每个位置都有可能的数字，但是如果有条件，那么就只能是条件的数字，如果有多个，那么就取最小的那个，如果这个数字是0，那么就不行，如果这个数字是第一位，那么就不行，如果这个数字是第一位，且是0，那么就不行，
