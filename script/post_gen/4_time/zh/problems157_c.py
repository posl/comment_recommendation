Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n,m = map(int,input().split())
    num = [0 for i in range(n)]
    for i in range(m):
        s,c = map(int,input().split())
        if num[s-1] != 0 and num[s-1] != c:
            print(-1)
            return
        num[s-1] = c
    if n != 1 and num[0] == 0:
        print(-1)
        return
    elif n == 1 and num[0] == 0:
        print(0)
        return
    else:
        if num[0] == 0:
            num[0] = 1
        print(''.join(map(str,num)))
        return

=======
Suggestion 2

def getNum(N, M, sc):
    # print(N, M, sc)
    # print(sc)
    # print(sc[0])
    # print(sc[0][0])
    # print(sc[0][1])
    # print(sc[1])
    # print(sc[1][0])
    # print(sc[1][1])
    # print(sc[2])
    # print(sc[2][0])
    # print(sc[2][1])
    # print(sc[3])
    # print(sc[3][0])
    # print(sc[3][1])
    # print(sc[4])
    # print(sc[4][0])
    # print(sc[4][1])
    # print(sc[5])
    # print(sc[5][0])
    # print(sc[5][1])
    # print(sc[6])
    # print(sc[6][0])
    # print(sc[6][1])
    # print(sc[7])
    # print(sc[7][0])
    # print(sc[7][1])
    # print(sc[8])
    # print(sc[8][0])
    # print(sc[8][1])
    # print(sc[9])
    # print(sc[9][0])
    # print(sc[9][1])
    # print(sc[10])
    # print(sc[10][0])
    # print(sc[10][1])
    # print(sc[11])
    # print(sc[11][0])
    # print(sc[11][1])
    # print(sc[12])
    # print(sc[12][0])
    # print(sc[12][1])
    # print(sc[13])
    # print(sc[13][0])
    # print(sc[13][1])
    # print(sc[14])
    # print(sc[14][0])
    # print(sc[14][1])
    # print(sc[15])
    # print(sc[15][0])
    # print(sc[15][1])
    # print(sc[16])
    # print(sc[16][0])
    # print(sc[16][1])
    # print(sc[17])
    # print(sc[17][0])
    # print(sc[17][1])
    # print(sc[18])
    # print(sc[18][0])
    # print(sc[18][1])
    # print

=======
Suggestion 3

def main():
    n,m=map(int,input().split())
    s=[0]*m
    c=[0]*m
    for i in range(m):
        s[i],c[i]=map(int,input().split())
    if n==1:
        if m==0:
            print(0)
        elif m==1:
            print(c[0])
        else:
            print(-1)
    elif n==2:
        if m==0:
            print(10)
        elif m==1:
            if s[0]==1:
                print(c[0]*10)
            elif s[0]==2:
                print(c[0]+10)
            else:
                print(-1)
        elif m==2:
            if s[0]==1 and s[1]==2 and c[0]==c[1]:
                print(c[0]*11)
            else:
                print(-1)
        else:
            print(-1)
    elif n==3:
        if m==0:
            print(100)
        elif m==1:
            if s[0]==1:
                print(c[0]*100)
            elif s[0]==2:
                print(c[0]*10+10)
            elif s[0]==3:
                print(c[0]+100)
            else:
                print(-1)
        elif m==2:
            if s[0]==1 and s[1]==2 and c[0]==c[1]:
                print(c[0]*110)
            elif s[0]==1 and s[1]==3 and c[0]==c[1]:
                print(c[0]*101)
            elif s[0]==2 and s[1]==3 and c[0]==c[1]:
                print(c[0]*11+10)
            else:
                print(-1)
        elif m==3:
            if s[0]==1 and s[1]==2 and s[2]==3 and c[0]==c[1] and c[1]==c[2]:
                print(c[0]*111)
            else:
                print(-1)
        else:
            print(-1)
    else:
        print(-1)

=======
Suggestion 4

def solve(n, m, sc):
    for i in range(10 ** (n - 1), 10 ** n):
        s = str(i)
        for j in range(m):
            if s[sc[j][0] - 1] != str(sc[j][1]):
                break
        else:
            return i
    return -1

=======
Suggestion 5

def main():
    # 读取输入
    n,m = map(int,input().split())
    # 保存输入
    s = []
    c = []
    # 读取输入
    for i in range(m):
        s_temp,c_temp = map(int,input().split())
        s.append(s_temp)
        c.append(c_temp)
    # 得到结果
    result = get_result(n,m,s,c)
    # 打印结果
    print(result)

=======
Suggestion 6

def main():
    N,M = map(int,input().split())
    s = [0 for i in range(M)]
    c = [0 for i in range(M)]
    for i in range(M):
        s[i],c[i] = map(int,input().split())
    if N == 1:
        for i in range(10):
            if i == c[0]:
                print(i)
                exit()
        print(-1)
        exit()
    if N == 2:
        for i in range(10):
            for j in range(10):
                if i == c[0] and j == c[1]:
                    print(i*10+j)
                    exit()
        print(-1)
        exit()
    if N == 3:
        for i in range(10):
            for j in range(10):
                for k in range(10):
                    if i == c[0] and j == c[1] and k == c[2]:
                        print(i*100+j*10+k)
                        exit()
        print(-1)
        exit()

=======
Suggestion 7

def main():
    N, M = map(int, input().split())
    s = []
    c = []
    for i in range(M):
        s_i, c_i = map(int, input().split())
        s.append(s_i)
        c.append(c_i)

    min_n = 10 ** (N - 1)
    max_n = 10 ** N - 1
    for n in range(min_n, max_n + 1):
        n = str(n)
        for i in range(M):
            if n[s[i] - 1] != str(c[i]):
                break
        else:
            print(n)
            break
    else:
        print(-1)

=======
Suggestion 8

def f(n, m, s, c):
    if m == 0:
        return -1
    if n == 1:
        if m == 1:
            return c[0]
        else:
            return -1
    if n == 2:
        if m == 1:
            return c[0] * 10 + c[1]
        elif m == 2:
            if s[0] == 1:
                return c[0] * 10 + c[1]
            else:
                return c[1] * 10 + c[0]
        else:
            return -1
    if n == 3:
        if m == 1:
            return c[0] * 100 + c[1] * 10 + c[2]
        elif m == 2:
            if s[0] == 1:
                return c[0] * 100 + c[1] * 10 + c[2]
            elif s[0] == 2:
                return c[1] * 100 + c[0] * 10 + c[2]
            else:
                return c[1] * 100 + c[2] * 10 + c[0]
        elif m == 3:
            if s[0] == 1:
                if s[1] == 2:
                    return c[0] * 100 + c[1] * 10 + c[2]
                else:
                    return c[0] * 100 + c[2] * 10 + c[1]
            elif s[0] == 2:
                if s[1] == 1:
                    return c[1] * 100 + c[0] * 10 + c[2]
                else:
                    return c[2] * 100 + c[0] * 10 + c[1]
            else:
                if s[1] == 1:
                    return c[1] * 100 + c[2] * 10 + c[0]
                else:
                    return c[2] * 100 + c[1] * 10 + c[0]
        else:
            return -1

=======
Suggestion 9

def main():
    n,m = map(int,input().split())
    #print(n,m)
    s = []
    c = []
    for i in range(m):
        s1,c1 = map(int,input().split())
        s.append(s1)
        c.append(c1)
    #print(s,c)
    if n == 1:
        print(c[0])
    elif n == 2:
        if s[0] == 1:
            print(str(c[0])+str(c[1]))
        else:
            print(str(c[1])+str(c[0]))
    elif n == 3:
        if s[0] == 1:
            print(str(c[0])+str(c[1])+str(c[2]))
        elif s[0] == 2:
            print(str(c[1])+str(c[0])+str(c[2]))
        else:
            print(str(c[1])+str(c[2])+str(c[0]))
    else:
        print(-1)

=======
Suggestion 10

def main():
    N,M = map(int, input().split())
    s = []
    c = []
    for i in range(M):
        s_i, c_i = map(int, input().split())
        s.append(s_i)
        c.append(c_i)

    #print(N,M,s,c)

    #从最小值开始
    for i in range(10**(N-1), 10**N):
        #print("i=",i)
        #print("i=",i)
        #print("str(i)=",str(i))
        #print("len(str(i))=",len(str(i)))
        #print("N=",N)
        if len(str(i)) == N:
            #print("len(str(i))=",len(str(i)))
            #print("N=",N)
            #print("i=",i)
            #print("str(i)=",str(i))
            #print("len(str(i))=",len(str(i)))
            #print("N=",N)
            #print("i=",i)
            #print("str(i)=",str(i))
            #print("len(str(i))=",len(str(i)))
            #print("N=",N)
            #print("i=",i)
            #print("str(i)=",str(i))
            #print("len(str(i))=",len(str(i)))
            #print("N=",N)
            #print("i=",i)
            #print("str(i)=",str(i))
            #print("len(str(i))=",len(str(i)))
            #print("N=",N)
            #print("i=",i)
            #print("str(i)=",str(i))
            #print("len(str(i))=",len(str(i)))
            #print("N=",N)
            #print("i=",i)
            #print("str(i)=",str(i))
            #print("len(str(i))=",len(str(i)))
            #print("N=",N)
            #print("i=",i)
            #print("str(i)=",str(i))
            #print("len(str(i))=",len(str(i)))
            #print("N=",N)
            #print("i=",i)
            #print("str(i)=",str(i))
            #print("len(str(i))=",len(str(i)))
            #print("N=",N)
            #print("i=",i)
            #print("str(i)
