Synthesizing 10/10 solutions (Duplicates hidden)

=======

def main():
    N, M, X, Y = map(int, input().split())
    x = list(map(int, input().split()))
    y = list(map(int, input().split()))
    if max(x) < min(y) and max(x) < Y and min(y) > X:
        print("No War")
    else:
        print("War")

=======

def main():
    n, m, x, y = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a.append(x)
    b.append(y)
    a.sort()
    b.sort()
    if a[-1] >= b[0]:
        print("War")
    else:
        print("No War")

=======

def main():
    N, M, X, Y = map(int, input().split())
    x = list(map(int, input().split()))
    y = list(map(int, input().split()))
    x_max = max(x)
    y_min = min(y)
    if x_max < y_min and X < y_min <= Y:
        print("No War")
    else:
        print("War")

=======

def main():
    n, m, x, y = map(int, input().split())
    xs = list(map(int, input().split()))
    ys = list(map(int, input().split()))
    xs.append(x)
    ys.append(y)
    xs.sort()
    ys.sort()
    if xs[-1] < ys[0]:
        print("No War")
    else:
        print("War")

main()

=======

def   main (): 
     # 入力受け取り 
     N ,   M ,   X ,   Y   =   map ( int ,   input (). split ()) 
     x   =   list ( map ( int ,   input (). split ())) 
     y   =   list ( map ( int ,   input (). split ())) 

     # Z を求める 
     Z   =   max ( X ,   max ( x )) 

     # Z が条件を満たすかどうか判定 
     if   Z   <   Y   and   min ( y )   >   Z : 
         print ( "No War" ) 
     else : 
         print ( "War" )

=======

def main():
    #入力
    N, M, X, Y = map(int, input().split())
    x = list(map(int, input().split()))
    y = list(map(int, input().split()))
    #条件を満たすZを探す
    z = X
    while z <= Y:
        z += 1
        if z in x or z in y:
            continue
        else:
            break
    #出力
    if z <= Y:
        print("No War")
    else:
        print("War")

=======

def main():
    #入力
    N, M, X, Y = map(int, input().split())
    x = list(map(int, input().split()))
    y = list(map(int, input().split()))
    #Zの候補をリストで作成
    z = [i for i in range(X+1, Y+1)]
    #Zの候補を全て見て条件を満たすか確認
    for i in z:
        if X < i <= Y and max(x) < i and min(y) >= i:
            print('No War')
            return
    print('War')

=======

def main():
    # A, Bの首都の座標
    N, M, X, Y = map(int, input().split())
    # A帝国の都市の座標
    A = list(map(int, input().split()))
    # B帝国の都市の座標
    B = list(map(int, input().split()))
    # X < Z <= Y
    # x_1, x_2, ..., x_N < Z
    # y_1, y_2, ..., y_M >= Z
    # となる Z が存在すれば、合意が成立して戦争は起きない
    # Z = max(x_i) + 1
    # Z = min(y_i) - 1

    # Zの候補
    Z = [max(A) + 1, min(B) - 1]
    # Zの候補の中で、X < Z <= Y となるものが存在すれば、合意が成立して戦争は起きない
    if max(Z) > X and min(Z) <= Y:
        print('No War')
    else:
        print('War')

=======

def solve():
    N,M,X,Y = map(int,input().split())
    x = list(map(int,input().split()))
    y = list(map(int,input().split()))
    #A帝国の座標Xより大きい値を持つxの要素のうち最小の値
    x_min = min([i for i in x if i > X])
    #B帝国の座標Yより小さい値を持つyの要素のうち最大の値
    y_max = max([i for i in y if i < Y])
    #x_minとy_maxの間にZが存在するかどうか
    if x_min <= y_max:
        print("No War")
    else:
        print("War")
