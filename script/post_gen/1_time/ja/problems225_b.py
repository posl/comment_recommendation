Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    a = [0] * (N-1)
    b = [0] * (N-1)
    for i in range(N-1):
        a[i], b[i] = map(int,input().split())
    if N == 3:
        if a[0] == a[1] or a[0] == b[1] or b[0] == a[1] or b[0] == b[1]:
            print("Yes")
        else:
            print("No")
    else:
        if a.count(1) == 1:
            print("Yes")
        else:
            print("No")

=======
Suggestion 2

def main():
    n = int(input())
    a = []
    b = []
    for i in range(n-1):
        a_i, b_i = map(int, input().split())
        a.append(a_i)
        b.append(b_i)
    a_set = set(a)
    b_set = set(b)
    if len(a_set) == 1:
        print("Yes")
    elif len(b_set) == 1:
        print("Yes")
    else:
        print("No")

=======
Suggestion 3

def main():
    N = int(input())
    A = [0 for i in range(N)]
    for i in range(N-1):
        a,b = map(int,input().split())
        A[a-1] += 1
        A[b-1] += 1
    if A.count(1) == 1 and A.count(N-1) == 1:
        print("Yes")
    else:
        print("No")

=======
Suggestion 4

def main():
    # 入力
    N = int(input())
    a = []
    b = []
    for i in range(N-1):
        a_i, b_i = map(int, input().split())
        a.append(a_i)
        b.append(b_i)
    
    # 処理
    # 頂点の次数を求める
    deg = [0] * (N+1)
    for i in range(N-1):
        deg[a[i]] += 1
        deg[b[i]] += 1
    
    # 出力
    if deg.count(N-1) == 1 and deg.count(1) == N-1:
        print('Yes')
    else:
        print('No')

=======
Suggestion 5

def main():
    N = int(input())
    node = [0] * N
    for i in range(N-1):
        a, b = map(int, input().split())
        node[a-1] += 1
        node[b-1] += 1
    if node.count(1) == 1:
        print("Yes")
    else:
        print("No")

=======
Suggestion 6

def main():
    n = int(input())
    a = [0 for i in range(n)]
    for i in range(n-1):
        x,y = map(int,input().split())
        a[x-1] += 1
        a[y-1] += 1
    if max(a) == n-1:
        print("Yes")
    else:
        print("No")

=======
Suggestion 7

def main():
    N = int(input())
    A = []
    B = []
    for i in range(N-1):
        a,b = map(int, input().split())
        A.append(a)
        B.append(b)
    #print(A)
    #print(B)
    A.sort()
    B.sort()
    #print(A)
    #print(B)
    if A[0] == 1 and B[N-2] == N:
        print("Yes")
    else:
        print("No")

=======
Suggestion 8

def main():
    N = int(input())
    A = []
    B = []
    for _ in range(N-1):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    if N-1 == max(A.count(i) for i in range(1, N+1)):
        print("Yes")
    else:
        print("No")

=======
Suggestion 9

def main():
    N = int(input())
    #各頂点の次数を格納するリスト
    deg = [0 for _ in range(N)]
    for _ in range(N-1):
        a,b = map(int,input().split())
        #頂点番号は1から始まっているので、1を引いて0から始まるようにする
        a -= 1
        b -= 1
        #a,bの次数をそれぞれ1増やす
        deg[a] += 1
        deg[b] += 1
    #次数がN-1の頂点が1つだけあればスター
    if deg.count(N-1) == 1:
        print('Yes')
    else:
        print('No')

=======
Suggestion 10

def main():
    N = int(input())
    edges = [list(map(int, input().split())) for _ in range(N-1)]
    #print(edges)
    #print(N)
    #print(edges)
    #print(edges[0])
    #print(edges[0][0])
    #print(edges[0][1])
    #print(edges[1])
    #print(edges[1][0])
    #print(edges[1][1])
    #print(edges[2])
    #print(edges[2][0])
    #print(edges[2][1])
    #print(edges[3])
    #print(edges[3][0])
    #print(edges[3][1])
    #print(edges[4])
    #print(edges[4][0])
    #print(edges[4][1])
    #print(edges[5])
    #print(edges[5][0])
    #print(edges[5][1])
    #print(edges[6])
    #print(edges[6][0])
    #print(edges[6][1])
    #print(edges[7])
    #print(edges[7][0])
    #print(edges[7][1])
    #print(edges[8])
    #print(edges[8][0])
    #print(edges[8][1])
    #print(edges[9])
    #print(edges[9][0])
    #print(edges[9][1])
    #print(edges[10])
    #print(edges[10][0])
    #print(edges[10][1])
    #print(edges[11])
    #print(edges[11][0])
    #print(edges[11][1])
    #print(edges[12])
    #print(edges[12][0])
    #print(edges[12][1])
    #print(edges[13])
    #print(edges[13][0])
    #print(edges[13][1])
    #print(edges[14])
    #print(edges[14][0])
    #print(edges[14][1])
    #print(edges[15])
    #print(edges[15][0])
    #print(edges[15][1])
    #print(edges[16])
    #print(edges[16][0])
    #print(edges[16][1])
    #print(edges[17])
    #print(edges[17][0])
    #print(edges[17][1])
    #print(edges[18])
