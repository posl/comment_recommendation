Synthesizing 10/10 solutions

=======
Suggestion 1

def gcd(a, b):
    if a < b:
        a, b = b, a
    while b != 0:
        a, b = b, a % b
    return a

=======
Suggestion 2

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

=======
Suggestion 3

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = [0] * 1001
    for i in range(n):
        b[a[i]] += 1
    ans = 0
    ans_num = 0
    for i in range(2, 1001):
        num = 0
        for j in range(i, 1001, i):
            num += b[j]
        if ans < num:
            ans = num
            ans_num = i
    print(ans_num)

=======
Suggestion 4

def main():
    n = int(input())
    a = list(map(int, input().split()))
    gcd = [0] * 1001
    for i in a:
        for j in range(1, i + 1):
            if i % j == 0:
                gcd[j] += 1
    print(gcd.index(max(gcd)))

=======
Suggestion 5

def gcd(a,b):
    if a<b:
        a,b = b,a
    while b>0:
        a,b = b,a%b
    return a

=======
Suggestion 6

def main():
    N = int(input())
    A = list(map(int, input().split()))
    #print(N)
    #print(A)

    #最大公約数を求める関数
    def gcd(a, b):
        if b == 0:
            return a
        else:
            return gcd(b, a % b)

    #最大公約数を求める
    g = A[0]
    for i in range(1, N):
        g = gcd(g, A[i])
    #print(g)

    #最大公約数の倍数を求める
    ans = []
    for i in range(1, 1000):
        if g % i == 0:
            ans.append(i)
    #print(ans)

    #最大公約数の倍数のうち、Aの要素に含まれるものを求める
    ans2 = []
    for i in ans:
        for j in A:
            if j % i == 0:
                ans2.append(i)
                break
    #print(ans2)

    #最大公約数の倍数のうち、Aの要素に含まれるもののうち、最大のものを求める
    ans3 = ans2[0]
    for i in ans2:
        if ans3 < i:
            ans3 = i
    #print(ans3)

    print(ans3)

=======
Suggestion 7

def gcd(a,b):
    while b:
        a,b = b,a%b
    return a

=======
Suggestion 8

def main():
    N=int(input())
    A=list(map(int,input().split()))
    B=[0]*1001
    for i in range(N):
        B[A[i]]+=1
    M=0
    for i in range(2,1001):
        C=0
        for j in range(i,1001,i):
            C+=B[j]
        if M<C:
            M=C
            ans=i
    print(ans)

=======
Suggestion 9

def main():
    N = int(input())
    A = list(map(int,input().split()))
    A.sort()
    if A[0] == 1:
        print(1)
        return
    else:
        GCD = A[0]
        for i in range(1,N):
            GCD = gcd(GCD,A[i])
        print(GCD)

=======
Suggestion 10

def main():
    n = int(input())
    a = list(map(int, input().split()))
    #print(n)
    #print(a)
    gcd_degree = 0
    gcd_degree_max = 0
    gcd_degree_max_num = 0
    for i in range(2, 1001):
        for j in range(0, n):
            if a[j] % i == 0:
                gcd_degree += 1
        if gcd_degree > gcd_degree_max:
            gcd_degree_max = gcd_degree
            gcd_degree_max_num = i
        gcd_degree = 0
    print(gcd_degree_max_num)
