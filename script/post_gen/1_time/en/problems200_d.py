Synthesizing 10/10 solutions

=======
Suggestion 1

def   main (): 
     N   =   int ( input ()) 
     A   =   list ( map ( int ,   input (). split ())) 
     mod200   =   [ []   for   _   in   range ( 200 )] 
     for   idx ,   a   in   enumerate ( A ): 
         mod200 [ a   %   200 ]. append ( idx + 1 ) 
     for   i   in   range ( 200 ): 
         if   len ( mod200 [ i ])   >=   2 : 
             print ( "Yes" ) 
             print ( len ( mod200 [ i ]),   * mod200 [ i ][: 2 ]) 
             print ( len ( mod200 [ i ]),   * mod200 [ i ][ 2 :]) 
             return 
     print ( "No" )

=======
Suggestion 2

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = [0] * 200
    for i in range(n):
        b[a[i] % 200] += 1
    for i in range(200):
        if b[i] >= 2:
            print('Yes')
            print(b[i])
            for j in range(n):
                if a[j] % 200 == i:
                    print(j + 1, end = ' ')
                    b[i] -= 1
                    if b[i] == 0:
                        print()
                        break
            print(b[i])
            for j in range(n):
                if a[j] % 200 == i:
                    print(j + 1, end = ' ')
                    b[i] -= 1
                    if b[i] == 0:
                        print()
                        break
            return
    print('No')

main()

=======
Suggestion 3

def solve():
    N = int(input())
    A = list(map(int, input().split()))
    mod = 200
    d = [[] for i in range(mod)]
    for i in range(N):
        d[A[i] % mod].append(i + 1)
    for i in range(mod):
        if len(d[i]) >= 2:
            print("Yes")
            print(1, d[i][0])
            print(1, d[i][1])
            return
    for i in range(mod):
        for j in range(i + 1, mod):
            if len(d[i]) >= 1 and len(d[j]) >= 1:
                print("Yes")
                print(2, d[i][0], d[j][0])
                print(1, d[i][0] if d[i][0] < d[j][0] else d[j][0])
                return
    print("No")

=======
Suggestion 4

def main():
    N = int(input())
    A = list(map(int, input().split()))
    MOD = 200
    D = dict()
    for i in range(N):
        key = A[i] % MOD
        if key not in D:
            D[key] = [i]
        else:
            D[key].append(i)
    for key in D:
        if len(D[key]) >= 2:
            print("Yes")
            print(1, D[key][0] + 1)
            print(1, D[key][1] + 1)
            return
    print("No")

=======
Suggestion 5

def  main():
    n = int(input())
    a = list(map(int, input().split()))
    b = {}
    for i in range(n):
        b[a[i] % 200] = i + 1
    for i in range(n):
        if b[(a[i] % 200)] != i + 1:
            print("Yes")
            print("1", i + 1)
            print("1", b[(a[i] % 200)])
            return
    print("No")

=======
Suggestion 6

def main():
    N = int(input())
    A = list(map(int, input().split()))
    #A = [int(x) for x in input().split()]
    #A = [int(x) for x in sys.stdin.readline().split()]
    #A = [int(x) for x in sys.stdin.readlines()[1].split()]

    #print(N)
    #print(A)

    A = [x % 200 for x in A]
    #pr

=======
Suggestion 7

def main():
    N = int(input())
    A = list(map(int, input().split()))
    # A_i mod 200
    mod = [a % 200 for a in A]
    # A_i mod 200の値に対応するindexを格納
    mod_index = [[] for _ in range(200)]
    for i in range(N):
        mod_index[mod[i]].append(i+1)
    # mod_index[i]の要素数が2以上であれば、それらの要素の和が200の倍数である
    for i in range(200):
        if len(mod_index[i]) >= 2:
            print('Yes')
            print(1, mod_index[i][0])
            print(len(mod_index[i])-1, *mod_index[i][1:])
            return
    print('No')

=======
Suggestion 8

def main():
    N = int(input())
    A = list(map(int, input().split()))
    # 200で割ったあまりの組み合わせを辞書で管理
    # key: あまり, value: そのあまりの数字のindexのリスト
    remainder = {}
    for i, a in enumerate(A):
        r = a % 200
        if r in remainder:
            print("Yes")
            print(len(remainder[r]), *remainder[r])
            print(1, i + 1)
            return
        remainder[r] = [i + 1]
    print("No")

=======
Suggestion 9

def main():
    n = int(input())
    a = list(map(int, input().split()))
    
    # 1. 200で割った余りごとにグループ分け
    # 2. 余りが0のグループについては、そのグループ内の要素が2つ以上あればYes
    # 3. 余りが0でないグループについては、同じ余りのグループが存在すればYes
    # 4. 余りが0でないグループについては、同じ余りのグループが存在しなければNo
    
    # 1. 200で割った余りごとにグループ分け
    # 2. 余りが0のグループについては、そのグループ内の要素が2つ以上あればYes
    # 3. 余りが0でないグループについては、同じ余りのグループが存在すればYes
    # 4. 余りが0でないグループについては、同じ余りのグループが存在しなければNo
    
    # 1. 200で割った余りごとにグループ分け
    # 2. 余りが0のグループについては、そのグループ内の要素が2つ以上あればYes
    # 3. 余りが0でないグループについては、同じ余りのグループが存在すればYes
    # 4. 余りが0でないグループについては、同じ余りのグループが存在しなければNo
    
    # 1. 200で割った余りごとにグループ分け
    # 2. 余りが0のグループについては、そのグループ内

=======
Suggestion 10

def main():
    N = int(input())
    A = list(map(int, input().split()))
    # 200個の空リストを作る
    # 0-199のリストを作る
    # それぞれのリストに、Aの中で割った余りが同じものがあれば、そのインデックスを入れる
    # その中で、2つ以上あれば、それらを出力する
    # なければ、Noを出力する
    B = [[] for _ in range(200)]
    for i, a in enumerate(A):
        B[a % 200].append(i + 1)
    for b in B:
        if len(b) >= 2:
            print("Yes")
            print("2")
            print(b[0], b[1])
            return
    print("No")
