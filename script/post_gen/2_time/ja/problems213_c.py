Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    H, W, N = map(int, input().split())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    A = list(set(A))
    B = list(set(B))
    A.sort()
    B.sort()
    for i in range(N):
        print(A.index(A[i])+1, B.index(B[i])+1)

=======
Suggestion 2

def main():
    H, W, N = map(int, input().split())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    #print(A)
    #print(B)
    A = sorted(A)
    B = sorted(B)
    #print(A)
    #print(B)
    #print(A[0])
    #print(B[0])
    for i in range(N):
        print(A.index(A[i]) + 1, B.index(B[i]) + 1)

=======
Suggestion 3

def main():
    H, W, N = map(int, input().split())
    A = [0] * N
    B = [0] * N
    for i in range(N):
        A[i], B[i] = map(int, input().split())
    #print(A)
    #print(B)
    A = list(set(A))
    B = list(set(B))
    #print(A)
    #print(B)
    A.sort()
    B.sort()
    #print(A)
    #print(B)
    for i in range(N):
        print(A.index(A[i]) + 1, B.index(B[i]) + 1)

=======
Suggestion 4

def main():
    H, W, N = map(int, input().split())
    A = [0] * N
    B = [0] * N
    for i in range(N):
        A[i], B[i] = map(int, input().split())
    A = list(set(A))
    B = list(set(B))
    A.sort()
    B.sort()
    for i in range(N):
        print(str(A.index(A[i]) + 1) + " " + str(B.index(B[i]) + 1))

=======
Suggestion 5

def main():
    H, W, N = map(int, input().split())
    A = [0] * N
    B = [0] * N
    for i in range(N):
        A[i], B[i] = map(int, input().split())

    # 重複を削除
    A = list(set(A))
    B = list(set(B))
    A.sort()
    B.sort()

    # 座標圧縮
    # 重複を削除した後の座標をキーとして、圧縮前の座標を値とする辞書を作成
    # 例えば、A = [1, 1, 3, 5, 5, 5, 7] のとき、A_dict = {1: 1, 3: 3, 5: 5, 7: 7} となる
    A_dict = {A[i]: i + 1 for i in range(len(A))}
    B_dict = {B[i]: i + 1 for i in range(len(B))}
    for i in range(N):
        print(A_dict[A[i]], B_dict[B[i]])

=======
Suggestion 6

def main():
    H, W, N = map(int, input().split())
    A = [0]*N
    B = [0]*N
    for i in range(N):
        A[i], B[i] = map(int, input().split())
    A = list(set(A))
    B = list(set(B))
    A.sort()
    B.sort()
    for i in range(N):
        print(A.index(A[i])+1, B.index(B[i])+1)

=======
Suggestion 7

def main():
    H, W, N = map(int, input().split())

    A = []
    B = []
    for _ in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)

    # 重複を削除
    A = list(set(A))
    B = list(set(B))

    # ソート
    A.sort()
    B.sort()

    # 座標を圧縮
    A = {a: i + 1 for i, a in enumerate(A)}
    B = {b: i + 1 for i, b in enumerate(B)}

    for a, b in zip(A, B):
        print(A[a], B[b])

=======
Suggestion 8

def main():
    H, W, N = map(int, input().split())
    A, B = [], []
    for n in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    
    #print(A)
    #print(B)
    
    #print(set(A))
    #print(set(B))
    
    #print(list(set(A)))
    #print(list(set(B)))
    
    #print(sorted(list(set(A))))
    #print(sorted(list(set(B))))
    
    #print(sorted(list(set(A)))[0])
    #print(sorted(list(set(B)))[0])
    
    #print(sorted(list(set(A)))[1])
    #print(sorted(list(set(B)))[1])
    
    #print(sorted(list(set(A)))[2])
    #print(sorted(list(set(B)))[2])
    
    #print(sorted(list(set(A)))[3])
    #print(sorted(list(set(B)))[3])
    
    #print(sorted(list(set(A)))[4])
    #print(sorted(list(set(B)))[4])
    
    #print(sorted(list(set(A)))[5])
    #print(sorted(list(set(B)))[5])
    
    #print(sorted(list(set(A)))[6])
    #print(sorted(list(set(B)))[6])
    
    #print(sorted(list(set(A)))[7])
    #print(sorted(list(set(B)))[7])
    
    #print(sorted(list(set(A)))[8])
    #print(sorted(list(set(B)))[8])
    
    #print(sorted(list(set(A)))[9])
    #print(sorted(list(set(B)))[9])
    
    #print(sorted(list(set(A)))[10])
    #print(sorted(list(set(B)))[10])
    
    #print(sorted(list(set(B)))[11])
    #print(sorted(list(set(B)))[11])
    
    #print(sorted(list(set(B)))[12])
    #print(sorted(list(set(B)))[12])
    
    #print(sorted(list(set(B)))[13])
    #print(sorted(list(set(B)))[13])
    
    #print(sorted(list(set(B)))[14])
    #print(sorted(list(set(B)))[14])
    
    #print(sorted(list(set(B)))[15])
    #print(sorted(list(set(B)))[15])
    
    #print(sorted(list(set(B)))[16])
    #print(sorted(list(set(B)))[16])

=======
Suggestion 9

def main():
    h, w, n = map(int, input().split())
    a = []
    b = []
    for i in range(n):
        a1, b1 = map(int, input().split())
        a.append(a1)
        b.append(b1)
    a = list(set(a))
    b = list(set(b))
    a.sort()
    b.sort()
    for i in range(n):
        print(a.index(a[i])+1, b.index(b[i])+1)

=======
Suggestion 10

def main():
    H,W,N = map(int,input().split())
    a_list = []
    b_list = []
    for i in range(N):
        a,b = map(int,input().split())
        a_list.append(a)
        b_list.append(b)
    a_list = list(set(a_list))
    b_list = list(set(b_list))
    a_list.sort()
    b_list.sort()
    a_dict = {}
    b_dict = {}
    for i in range(len(a_list)):
        a_dict[a_list[i]] = i+1
    for i in range(len(b_list)):
        b_dict[b_list[i]] = i+1
    for i in range(N):
        print(a_dict[a_list[i]],b_dict[b_list[i]])
