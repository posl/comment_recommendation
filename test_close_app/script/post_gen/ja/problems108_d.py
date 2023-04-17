Synthesizing 10/10 solutions

=======

def solve():
    L = int(input())
    print(8, 10)
    print(1, 2, 0)
    print(2, 3, 0)
    print(3, 4, 0)
    print(1, 5, 0)
    print(2, 6, 0)
    print(3, 7, 0)
    print(4, 8, 0)
    print(5, 6, 1)
    print(6, 7, 1)
    print(7, 8, 1)

=======

def main():
    L = int(input())
    if L == 2:
        print(2, 1)
        print(1, 2, 1)
    elif L == 3:
        print(3, 2)
        print(1, 2, 1)
        print(2, 3, 1)
    else:
        print(2 * L - 1, 2 * L)
        for i in range(1, L):
            print(i, i + 1, 0)
        for i in range(1, L):
            print(i, i + L, 2 * i - 1)
        print(L, 2 * L - 1, L - 1)

=======

def main():
    L = int(input())
    N = 20
    M = 60
    print(N, M)
    for i in range(N-1):
        print(i+1, i+2, 0)
    for i in range(N-1):
        print(i+1, i+2, 10**6)
    for i in range(L):
        print(i+1, i+2, 1)

=======

def main():
    L = int(input())
    print(20, 60)
    for i in range(1, 20):
        print(i, i+1, 0)
        print(i, i+1, 10**6)
    for i in range(1, 11):
        print(i, i+10, 10**6 - i)
        print(i, i+10, 10**6 + i)
    for i in range(1, 11):
        print(i, i+10, L-1)

=======

def main():
    L = int(input())
    N = 20
    M = 60
    print(N, M)
    for i in range(1, N):
        print(i, i+1, 0)
    for i in range(1, N):
        print(i, i+1, 10**6)
    for i in range(1, N):
        for j in range(1, N):
            if i != j:
                print(i, j, 10**6+i+j)

=======

def main():
    L = int(input())
    N = 20
    M = 60
    print(N, M)
    for i in range(1, N):
        print(i, i+1, 0)
    for i in range(1, N):
        print(i, i+1, 2**i)
    for i in range(1, N-1):
        print(i, i+2, 2**(i+1))
    for i in range(1, N):
        if 2**i-1 <= L:
            print(1, i+1, L-2**i+1)
        else:
            print(1, i+1, 0)

main()

=======

def main():
    L = int(input())
    print(20, 30)
    for i in range(1, 20):
        print(i, i+1, 0)
        print(i, i+1, 10**6)
    for i in range(1, 11):
        print(i, i+10, L-i)

=======

def main():
    L = int(input())
    N = L+3
    M = N-1
    print(N, M)
    for i in range(M):
        print(i+1, i+2, 0)
    print(1, 3, L)

=======

def main():
    L = int(input())
    print("3 3")
    print("1 2", 2*L+1)
    print("2 3", 2*L)
    print("1 3", 2*L+1)

=======

def main():
    L = int(input())
    N = 20
    #各パスの長さを求める
    #パスの長さは、そのパス上の辺の長さの和を表す
    #0からL-1までの相異なる整数である
    #パスの長さが0のものは、パスの始点と終点が同じである
    #パスの長さが1のものは、パスの始点と終点が隣り合っている
    #パスの長さが2のものは、パスの始点と終点が2つ離れた頂点である
    #パスの長さが3のものは、パスの始点と終点が3つ離れた頂点である
    #パスの長さが4のものは、パスの始点と終点が4つ離れた頂点である
    #パスの長さが5のものは、パスの始点と終点が5つ離れた頂点である
    #パスの長さが6のものは、パスの始点と終点が6つ離れた頂点である
    #パスの長さが7のものは、パスの始点と終点が7つ離れた頂点である
    #パスの長さが8のものは、パスの始点と終点が8つ離れた頂点である
    #パスの長さが9のものは、パスの始点と終点が9つ離れた頂点である
    #パスの長さが10のものは、パスの始点と終点が10つ離れた頂点である
    #パスの長さが11のものは、パス
