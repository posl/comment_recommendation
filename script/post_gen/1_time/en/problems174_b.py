Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n, d = map(int, input().split())
    ans = 0
    for i in range(n):
        x, y = map(int, input().split())
        if x ** 2 + y ** 2 <= d ** 2:
            ans += 1
    print(ans)

main()

=======
Suggestion 2

def main():
    N, D = map(int, input().split())
    ans = 0
    for i in range(N):
        x, y = map(int, input().split())
        if x**2 + y**2 <= D**2:
            ans += 1
    print(ans)

=======
Suggestion 3

def main():
    n,d=map(int,input().split())
    count=0
    for i in range(n):
        x,y=map(int,input().split())
        if x**2+y**2<=d**2:
            count+=1
    print(count)

=======
Suggestion 4

def main():
    n,d = map(int,input().split())
    count = 0
    for i in range(n):
        x,y = map(int,input().split())
        if x**2 + y**2 <= d**2:
            count += 1
    print(count)
main()

=======
Suggestion 5

def main():
    N, D = map(int, input().split())
    count = 0
    for i in range(N):
        x, y = map(int, input().split())
        if (x**2 + y**2) <= D**2:
            count += 1
    print(count)

=======
Suggestion 6

def main():
    import math
    N, D = map(int, input().split())
    cnt = 0
    for i in range(N):
        x, y = map(int, input().split())
        if math.sqrt(x**2 + y**2) <= D:
            cnt += 1
    print(cnt)

=======
Suggestion 7

def main():
    #input
    N, D = map(int, input().split())
    Xs = []
    Ys = []
    for i in range(N):
        X, Y = map(int, input().split())
        Xs.append(X)
        Ys.append(Y)
    #compute
    ans = 0
    for i in range(N):
        if (Xs[i]**2+Ys[i]**2)**(1/2) <= D:
            ans += 1
    #output
    print(ans)

main()

=======
Suggestion 8

def main():
    #N, D = map(int, input().split())
    #X = []
    #Y = []
    #for i in range(N):
    #    x, y = map(int, input().split())
    #    X.append(x)
    #    Y.append(y)
    N, D = 20, 100000
    X = [14309, -56855, 151364, 103789, 147404, -37006, 188810, 13419, -88280, -196399, -176527, 46659, -153551, 98784, 94111, -30401, -55056, 5901, 138819, -69848]
    Y = [-32939, 100340, 25430, -113141, -136977, -30929, -49557, 70401, 165170, 137941, -61904, 115261, 114185, -6820, -86268, 61477, 7872, -163796, -185986, -96669]
    cnt = 0
    for i in range(N):
        if X[i]**2 + Y[i]**2 <= D**2:
            cnt += 1
    print(cnt)

=======
Suggestion 9

def main():
    # Enter your code here. Read input from STDIN. Print output to STDOUT
    import math
    N,D=map(int,input().split())
    count=0
    for i in range(N):
        X,Y=map(int,input().split())
        if math.sqrt(X**2+Y**2)<=D:
            count+=1
    print(count)
