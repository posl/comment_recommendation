Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n,c = map(int,input().split())
    a = []
    b = []
    d = []
    for i in range(n):
        a1,b1,d1 = map(int,input().split())
        a.append(a1)
        b.append(b1)
        d.append(d1)
    total = 0
    for i in range(n):
        total += d[i]
    print(total)
    return total

=======
Suggestion 2

def main():
    N, C = map(int, input().split())
    #print(N, C)
    A = []
    B = []
    C = []
    for i in range(N):
        a, b, c = map(int, input().split())
        A.append(a)
        B.append(b)
        C.append(c)
    #print(A, B, C)
    #print(type(A[0]))
    #print(type(B[0]))
    #print(type(C[0]))
    #print(type(N))
    #print(type(C))
    #print(type(A))
    #print(type(B))
    #print(type(N))
    #print(type(C))
    #print(type(A))
    #print(type(B))
    #print(type(C))
    #print(type(N))
    #print(type(C))
    #print(type(A))
    #print(type(B))
    #print(type(C))
    #print(type(N))
    #print(type(C))
    #print(type(A))
    #print(type(B))
    #print(type(C))
    #print(type(N))
    #print(type(C))
    #print(type(A))
    #print(type(B))
    #print(type(C))
    #print(type(N))
    #print(type(C))
    #print(type(A))
    #print(type(B))
    #print(type(C))
    #print(type(N))
    #print(type(C))
    #print(type(A))
    #print(type(B))
    #print(type(C))
    #print(type(N))
    #print(type(C))
    #print(type(A))
    #print(type(B))
    #print(type(C))
    #print(type(N))
    #print(type(C))
    #print(type(A))
    #print(type(B))
    #print(type(C))
    #print(type(N))
    #print(type(C))
    #print(type(A))
    #print(type(B))
    #print(type(C))
    #print(type(N))
    #print(type(C))
    #print(type(A))
    #print(type(B))
    #print(type(C))
    #print(type(N))
    #print(type(C))
    #print(type(A))
    #print(type(B))
    #print(type(C))
    #print(type(N))
    #print(type(C))
    #print(type(A))
    #print(type(B))
    #print(type(C))
    #print(type(N))
    #print(type(C))

=======
Suggestion 3

def main():
    n,c = map(int,input().split())
    a,b,cc = [0]*n,[0]*n,[0]*n
    for i in range(n):
        a[i],b[i],cc[i] = map(int,input().split())
        b[i] += 1
    d = [0]*(10**9+2)
    for i in range(n):
        d[a[i]] += cc[i]
        d[b[i]] -= cc[i]
    for i in range(10**9+1):
        d[i+1] += d[i]
    print(min(c,min(d[1:])))

main()

=======
Suggestion 4

def main():
    # 读入数据
    N, C = map(int, input().split())
    # 服务开始时间
    A = []
    # 服务结束时间
    B = []
    # 服务费用
    C = []
    for i in range(N):
        a, b, c = map(int, input().split())
        A.append(a)
        B.append(b)
        C.append(c)
    # 找到最晚结束的服务
    maxB = max(B)
    # 计算每日费用
    dailyFee = [0] * (maxB + 1)
    for i in range(N):
        for j in range(A[i], B[i] + 1):
            dailyFee[j] += C[i]
    # 计算最小费用
    minFee = sum(C)
    for i in range(1, maxB + 1):
        if dailyFee[i] < minFee:
            minFee = dailyFee[i]
    print(minFee)

=======
Suggestion 5

def main():
    n,c = map(int,input().split())
    a = []
    b = []
    d = []
    for i in range(n):
        ai,bi,ci = map(int,input().split())
        a.append(ai)
        b.append(bi)
        d.append(ci)
    sum = 0
    for i in range(n):
        sum += d[i] * (b[i] - a[i] + 1)
    if sum < c:
        print(sum)
    else:
        print(c)

=======
Suggestion 6

def main():
    N, C = map(int, input().split(' '))
    ABC = []
    for i in range(N):
        ABC.append(list(map(int, input().split(' '))))
    ABC.sort(key=lambda x:x[0])

    ans = 0
    for i in range(N):
        ans += ABC[i][2] * (ABC[i][1] - ABC[i][0] + 1)
    print(ans)

=======
Suggestion 7

def main():
    n,c = map(int,input().split())
    s = []
    e = []
    p = []
    for i in range(n):
        a,b,d = map(int,input().split())
        s.append(a)
        e.append(b)
        p.append(d)
    s_e = list(zip(s,e,p))
    s_e.sort()
    s_e.append([c+1,c+1,0])
    #print(s_e)
    #print(s)
    #print(e)
    #print(p)
    p_sum = 0
    p_max = 0
    for i in range(n):
        if s_e[i][1] == s_e[i+1][0]:
            p_sum += s_e[i][2]
            if p_max < p_sum:
                p_max = p_sum
        else:
            p_sum += s_e[i][2]
            if p_max < p_sum:
                p_max = p_sum
            p_sum = 0
    print(p_max)

=======
Suggestion 8

def main():
    n, c = map(int, input().split())
    a = []
    b = []
    for i in range(n):
        a_i, b_i, c_i = map(int, input().split())
        a.append(a_i)
        b.append(b_i)
    print(n, c)
    print(a)
    print(b)

=======
Suggestion 9

def readinput():
    n,c=list(map(int,input().split()))
    abclist=[]
    for _ in range(n):
        abc=list(map(int,input().split()))
        abclist.append(abc)
    return n,c,abclist

=======
Suggestion 10

def main():
    n,c = map(int, input().split())
    data = []
    for i in range(n):
        data.append(list(map(int, input().split())))
    #print(data)
    #data = [[1, 2, 4], [2, 2, 4]]
    #data = [[583563238, 820642330, 44577], [136809000, 653199778, 90962], [54601291, 785892285, 50554], [5797762, 453599267, 65697], [468677897, 916692569, 87409]]
    #data = [[583563238, 820642330, 44577], [136809000, 653199778, 90962], [54601291, 785892285, 50554], [5797762, 453599267, 65697], [468677897, 916692569, 87409]]
    #data = [[583563238, 820642330, 44577], [136809000, 653199778, 90962], [54601291, 785892285, 50554], [5797762, 453599267, 65697], [468677897, 916692569, 87409]]
    #data = [[583563238, 820642330, 44577], [136809000, 653199778, 90962], [54601291, 785892285, 50554], [5797762, 453599267, 65697], [468677897, 916692569, 87409]]
    #data = [[583563238, 820642330, 44577], [136809000, 653199778, 90962], [54601291, 785892285, 50554], [5797762, 453599267, 65697], [468677897, 916692569, 87409]]
    #data = [[583563238, 820642330, 44577], [136809000, 653199778, 90962], [54601291, 785892285, 50554], [5797762, 453599267, 65697], [468677897, 916692
