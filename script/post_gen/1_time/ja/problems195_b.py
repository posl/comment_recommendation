Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    A, B, W = map(int, input().split())
    W *= 1000
    min = W // B
    max = W // A
    if W % B != 0:
        min += 1
    if W % A != 0:
        max -= 1
    if min > max:
        print("UNSATISFIABLE")
    else:
        print(min, max)

=======
Suggestion 2

def main():
    A, B, W = map(int, input().split())
    W *= 1000
    min_n = W // B
    max_n = W // A
    if W % B != 0:
        min_n += 1
    if W % A != 0:
        max_n -= 1
    if min_n > max_n:
        print("UNSATISFIABLE")
    else:
        print(min_n, max_n)

main()

=======
Suggestion 3

def main():
    A, B, W = map(int, input().split())
    W *= 1000
    if W % B == 0:
        min = W // B
    else:
        min = W // B + 1
    max = W // A
    if min > max:
        print('UNSATISFIABLE')
    else:
        print(min, max)

=======
Suggestion 4

def main():
    A, B, W = map(int, input().split())
    W *= 1000
    min = W // B
    max = W // A
    if min * B == W:
        print(min, max)
    elif max * A <= W:
        print(min + 1, max)
    else:
        print('UNSATISFIABLE')

main()

=======
Suggestion 5

def main():
    a,b,w = map(int,input().split())
    w *= 1000
    max = w//a
    min = w//b
    if w%b != 0:
        min += 1
    if max < min:
        print("UNSATISFIABLE")
    else:
        print(min,max)

=======
Suggestion 6

def main():
    A,B,W = map(int, input().split())
    W *= 1000
    ans = []
    for i in range(1,1001):
        if A*i <= W <= B*i:
            ans.append(i)
    if ans == []:
        print("UNSATISFIABLE")
    else:
        print(ans[0], ans[-1])

=======
Suggestion 7

def main():
    A,B,W = map(int, input().split())
    W = W * 1000
    #print(A)
    #print(B)
    #print(W)
    min = 0
    max = 0
    for i in range(1, W+1):
        if A*i <= W and W <= B*i:
            min = i
            break
    for i in range(W, 0, -1):
        if A*i <= W and W <= B*i:
            max = i
            break
    if min == 0:
        print("UNSATISFIABLE")
    else:
        print(min, max)

=======
Suggestion 8

def main():
    A,B,W = map(int, input().split())
    W *= 1000
    num_min = 0
    num_max = 0
    for i in range(1,1001):
        if A * i <= W <= B * i:
            num_min = i
            break
    for i in range(1000,0,-1):
        if A * i <= W <= B * i:
            num_max = i
            break
    if num_min == 0 and num_max == 0:
        print("UNSATISFIABLE")
    else:
        print(num_min,num_max)

=======
Suggestion 9

def main():
    # 標準入力から A,B,Wを取得
    A,B,W = map(int,input().split())
    # Wをキログラムからグラムに変換
    W = W * 1000
    # 最小値と最大値を初期化
    min = 0
    max = 0
    # 最小値を求める
    if W % B == 0:
        min = int(W / B)
    else:
        min = int(W / B) + 1
    # 最大値を求める
    if W % A == 0:
        max = int(W / A)
    else:
        max = int(W / A) + 1
    # 最小値と最大値を出力
    if min <= max:
        print(min,max)
    else:
        print("UNSATISFIABLE")

=======
Suggestion 10

def main():
    a, b, w = map(int, input().split())
    w *= 1000
    # a <= x <= b
    # a*x <= w <= b*x
    # x <= w/a <= x <= w/b
    min_x = w // b
    max_x = w // a
    if min_x * a <= w <= max_x * b:
        print(min_x, max_x)
    else:
        print("UNSATISFIABLE")

main()
