Synthesizing 9/10 solutions

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
    while b:
        a, b = b, a % b
    return a

=======
Suggestion 3

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

=======
Suggestion 4

def main():
    N = int(input())
    x = []
    y = []
    for _ in range(N):
        x_i, y_i = map(int, input().split())
        x.append(x_i)
        y.append(y_i)
    #print(x)
    #print(y)
    
    # (a, b) について、(x_i + a, y_i + b) が全て異なるような a, b の組み合わせを求める
    # これは、(x_i + a, y_i + b) が全て異なるような a, b の組み合わせが 2N 個以上あればいい
    # これは、(x_i, y_i) が全て異なるような a, b の組み合わせが N 個以上あればいい
    # これは、(x_i, y_i) が全て異なるような a, b の組み合わせが N 個以上あればいい
    # (x_i, y_i) が全て異なるような a, b の組み合わせは、(x_i - x_j, y_i - y_j) が全て異なるような a, b の組み合わせが N 個以上あればいい
    # (x_i, y_i) が全て異なるような a, b の組み合わせは、(x_i - x_j, y_i - y_j) が全て異なるような a, b の組み合わせが N 個以上あればいい
    # (x_i, y_i) が全て異なるような a, b の組み合わせは、(x_i - x_j, y_i - y_j) が全て異なるような a, b の組み合わせが N 個以上あればいい
    # (x_i, y_i) が全

=======
Suggestion 5

def main():
    N = int(input())
    XY = [list(map(int, input().split())) for _ in range(N)]
    D = {}
    for i in range(N):
        for j in range(i+1, N):
            x1, y1 = XY[i]
            x2, y2 = XY[j]
            d = (x2-x1, y2-y1)
            if d in D:
                D[d] += 1
            else:
                D[d] = 1
    ans = N-1
    for v in D.values():
        ans = min(ans, N-v)
    print(ans)

=======
Suggestion 6

def  main():
    n  =  int (input())
    x  =  [ 0 ] * n
    y  =  [ 0 ] * n
    for  i  in  range(n):
        x[i], y[i]  =  map( int , input().split())

    s  =  set ()
    for  i  in  range(n):
        for  j  in  range(n):
            if  i  ==  j:  continue 
            s.add((x[i] - x[j], y[i] - y[j]))
    print( len (s))

=======
Suggestion 7

def main():
    n = int(input())
    towns = []
    for i in range(n):
        towns.append(tuple(map(int, input().split())))
    ans = 0
    for i in range(n):
        for j in range(i+1, n):
            x = towns[i][0] - towns[j][0]
            y = towns[i][1] - towns[j][1]
            ans = max(ans, x*x + y*y)
    print(ans)

=======
Suggestion 8

def find_gcd(x, y):
    while(y):
        x, y = y, x % y
    return x

=======
Suggestion 9

def f(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])
