Synthesizing 10/10 solutions

=======
Suggestion 1

def   main (): 
     N   =   int ( input ()) 
     A   =   list ( map ( int ,   input (). split ())) 
     A   =   [ a   %   200   for   a   in   A ] 

     dp   =   [ 0   for   _   in   range ( 200 )] 
     for   i   in   range ( N ): 
         dp2   =   [ 0   for   _   in   range ( 200 )] 
         for   j   in   range ( 200 ): 
             dp2 [( j   +   A [ i ])   %   200 ]   =   dp [ j ] 
             dp2 [ j ]   =   max ( dp2 [ j ],   dp [ j ]) 
         dp2 [ A [ i ]]   =   max ( dp2 [ A [ i ]],   1 ) 
         dp   =   dp2 

     if   max ( dp )   <   2 : 
         print ( 'No' ) 
     else : 
         print ( 'Yes' ) 
         x   =   dp . index ( 1 ) 
         y   =   dp . index ( 2 ) 
         B   =   [] 
         C   =   [] 
         for   i   in   range ( N ): 
             if   A [ i ]   ==   x : 
                 B . append ( i   +   1 ) 
             elif   A [ i ]   ==   y : 
                 C . append ( i   +   1 ) 
         print ( len ( B ),   ' ' . join ( map ( str ,   B ))) 
         print ( len ( C ),   ' ' . join ( map ( str ,   C )))

=======
Suggestion 2

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    for i in range(n):
        for j in range(i+1, n):
            if (a[i] + a[j]) % 200 == 0:
                print("Yes")
                print(1, i+1)
                print(1, j+1)
                return
    print("No")
    return

=======
Suggestion 3

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = [0] * N
    C = [0] * N
    for i in range(N):
        B[i] = A[i] % 200
    for i in range(N):
        C[i] = A[i] % 200
    B.sort()
    C.sort()
    for i in range(N):
        if B[i] == C[i]:
            print("No")
            return
    print("Yes")
    for i in range(N):
        print(B[i], end=" ")
    print()
    for i in range(N):
        print(C[i], end=" ")
    print()

=======
Suggestion 4

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = []
    c = []
    for i in range(n):
        for j in range(i+1, n):
            if (a[i] + a[j]) % 200 == 0:
                b.append(i+1)
                c.append(j+1)
    if len(b) == 0:
        print("No")
    else:
        print("Yes")
        print(len(b))
        print(*b)
        print(len(c))
        print(*c)

=======
Suggestion 5

def main():
    N = int(input())
    A = [int(i) for i in input().split()]
    B = []
    C = []
    for i in range(N):
        for j in range(i+1, N):
            if A[i] % 200 == A[j] % 200:
                B = [i+1, j+1]
                C = [i+1, j+1]
    if B == []:
        print("No")
    else:
        print("Yes")
        print(len(B), *B, sep=" ")
        print(len(C), *C, sep=" ")
    return

=======
Suggestion 6

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = []
    C = []
    for i in range(N):
        B.append([A[i] % 200, i])
    B.sort()
    for i in range(N-1):
        if B[i][0] == B[i+1][0]:
            C.append(B[i][1]+1)
            C.append(B[i+1][1]+1)
            break
    if len(C) == 0:
        print('No')
    else:
        print('Yes')
        print(len(C))
        print(*C)
        print(len(C))
        print(*C)

=======
Suggestion 7

def main():
    N = int(input())
    A = list(map(int, input().split()))
    mod = 200
    mod_dict = {}
    for i, a in enumerate(A):
        mod_a = a % mod
        if mod_a in mod_dict:
            print("Yes")
            print(i + 1, *mod_dict[mod_a])
            print(i + 1, *[j + 1 for j in range(N) if j not in mod_dict[mod_a]])
            return
        else:
            mod_dict[mod_a] = [i]
    print("No")

=======
Suggestion 8

def solve():
    N = int(input())
    A = list(map(int, input().split()))
    if N > 200:
        print("No")
        return
    mod200 = [0] * 200
    for i in range(N):
        mod200[A[i] % 200] += 1
    for i in range(200):
        if mod200[i] >= 2:
            print("Yes")
            print(mod200[i], end=" ")
            for j in range(N):
                if A[j] % 200 == i:
                    print(j + 1, end=" ")
                    mod200[i] -= 1
                    if mod200[i] == 0:
                        break
            print()
            print(mod200[i], end=" ")
            for j in range(N):
                if A[j] % 200 == i:
                    print(j + 1, end=" ")
                    mod200[i] -= 1
                    if mod200[i] == 0:
                        break
            print()
            return
    print("No")
    return

=======
Suggestion 9

def main():
    N = int(input())
    A = list(map(int, input().split()))
    # A[i] % 200 に対応する i を格納する配列
    modA = [[] for _ in range(200)]
    for i in range(N):
        modA[A[i] % 200].append(i + 1)
    for i in range(200):
        if len(modA[i]) >= 2:
            print("Yes")
            print(1, modA[i][0])
            print(1, modA[i][1])
            return
    print("No")

=======
Suggestion 10

def main():
    N = int(input())
    A = list(map(int, input().split()))
    # mod200の値をとるときのindexを保持するリスト
    mod200 = [[] for _ in range(200)]
    # それぞれのmod200の値に対して、indexをmod200のリストに追加する
    for i, a in enumerate(A):
        mod200[a % 200].append(i + 1)
    # mod200の値が2以上ある場合、そのindexの組み合わせを出力する
    for m in mod200:
        if len(m) >= 2:
            print('Yes')
            print(1, m[0])
            print(1, m[1])
            return
    # mod200の値が2以上ない場合、mod200の値をとるときのindexを保持するリスト
    mod200 = [[] for _ in range(200)]
    # それぞれのmod200の値に対して、indexをmod200のリストに追加する
    for i, a in enumerate(A):
        mod200[a % 200].append(i + 1)
    # mod200の値が2以上ある場合、そのindexの組み合わせを出力する
    for m in mod200:
        if len(m) >= 2:
            print('Yes')
            print(1, m[0])
            print(1, m[1])
            return
    # mod200の値が2以上ない場合、Noを出力する
    print('No')
