Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def f1():
    N,A,B = map(int, input().split())
    P,Q,R,S = map(int, input().split())
    #print(N,A,B,P,Q,R,S)
    #print('N=%d,A=%d,B=%d,P=%d,Q=%d,R=%d,S=%d'%(N,A,B,P,Q,R,S))
    #print('N=%d,A=%d,B=%d,P=%d,Q=%d,R=%d,S=%d'%(N,A,B,P,Q,R,S))
    #print('N=%d,A=%d,B=%d,P=%d,Q=%d,R=%d,S=%d'%(N,A,B,P,Q,R,S))
    #print('N=%d,A=%d,B=%d,P=%d,Q=%d,R=%d,S=%d'%(N,A,B,P,Q,R,S))
    #print('N=%d,A=%d,B=%d,P=%d,Q=%d,R=%d,S=%d'%(N,A,B,P,Q,R,S))
    #print('N=%d,A=%d,B=%d,P=%d,Q=%d,R=%d,S=%d'%(N,A,B,P,Q,R,S))
    #print('N=%d,A=%d,B=%d,P=%d,Q=%d,R=%d,S=%d'%(N,A,B,P,Q,R,S))
    #print('N=%d,A=%d,B=%d,P=%d,Q=%d,R=%d,S=%

=======
Suggestion 2

def main():
    n, a, b = map(int, input().split())
    p, q, r, s = map(int, input().split())
    for i in range(p, q + 1):
        for j in range(r, s + 1):
            if (i + j) % 2 == (a + b) % 2:
                print('#', end='')
            else:
                print('.', end='')
        print()

=======
Suggestion 3

def main():
    pass

=======
Suggestion 4

def paint(a,b,n):
    #a,b表示起始点的坐标，n表示方块的大小
    for i in range(a,a+n):
        for j in range(b,b+n):
            if i+j == a+b+n-1:
                print('#',end='')
            else:
                print('.',end='')
        print()

=======
Suggestion 5

def main():
    #读取数据
    n,a,b = map(int,input().split())
    p,q,r,s = map(int,input().split())
    #初始化
    #矩阵
    matrix = [['.' for i in range(n)] for j in range(n)]
    #计算最大最小值
    min1 = min(1-a,1-b)
    max1 = max(n-a,n-b)
    min2 = min(1-a,b-n)
    max2 = max(n-a,b-1)
    #对矩阵进行填充
    for i in range(min1,max1+1):
        matrix[a+i-1][b+i-1] = '#'
    for i in range(min2,max2+1):
        matrix[a+i-1][b-i-1] = '#'
    #输出结果
    for i in range(p-1,q):
        print(''.join(matrix[i][r-1:s]))

=======
Suggestion 6

def main():
    n, a, b = map(int, input().split())
    p, q, r, s = map(int, input().split())
    for i in range(p, q+1):
        for j in range(r, s+1):
            if (max(1-a, 1-b) <= i-j <= min(n-a, n-b)) or (max(1-a, b-n) <= i+j <= min(n-a, b-1)):
                print('#', end='')
            else:
                print('.', end='')
        print()

=======
Suggestion 7

def solve(n, a, b, p, q, r, s):
    #print("n=%d, a=%d, b=%d, p=%d, q=%d, r=%d, s=%d" % (n, a, b, p, q, r, s))
    ret = []
    for i in range(p, q+1):
        ret.append([])
        for j in range(r, s+1):
            ret[i-p].append('.')
    for k in range(max(1-a, 1-b), min(n-a, n-b)+1):
        ret[a+k-p][b+k-r] = '#'
    for k in range(max(1-a, b-n), min(n-a, b-1)+1):
        ret[a+k-p][b-k-r] = '#'
    for k in range(max(a-n, 1-b), min(a-1, n-b)+1):
        ret[a-k-p][b+k-r] = '#'
    for k in range(max(a-n, b-n), min(a-1, b-1)+1):
        ret[a-k-p][b-k-r] = '#'
    for i in range(q-p+1):
        print(''.join(ret[i]))

=======
Suggestion 8

def main():
    N, A, B = map(int, input().split())
    P, Q, R, S = map(int, input().split())
    for i in range(P, Q+1):
        for j in range(R, S+1):
            if (i+j)%2 == (A+B)%2:
                print('#', end='')
            else:
                print('.', end='')
        print()
