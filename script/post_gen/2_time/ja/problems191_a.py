Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    v, t, s, d = map(int, input().split())
    if v * t <= d <= v * s:
        print("No")
    else:
        print("Yes")

=======
Suggestion 2

def main():
    V, T, S, D = map(int, input().split())
    if V * T <= D <= V * S:
        print("No")
    else:
        print("Yes")

=======
Suggestion 3

def main():
    v, t, s, d = map(int, input().split())
    if t * v <= d <= s * v:
        print('No')
    else:
        print('Yes')

=======
Suggestion 4

def main():
    V, T, S, D = map(int, input().split())
    if V*T <= D <= V*S:
        print('No')
    else:
        print('Yes')

=======
Suggestion 5

def main():
    V, T, S, D = map(int, input().split())
    if D < V*T or V*S < D:
        print("Yes")
    else:
        print("No")

=======
Suggestion 6

def main():
    V, T, S, D = map(int, input().split())
    if (D < V*T) or (D > V*S):
        print("Yes")
    else:
        print("No")

=======
Suggestion 7

def main():
    # 標準入力を取得
    V, T, S, D = map(int,input().split())
    # 高橋君が投げたボールが消える時間を計算
    disappear_time = V * T
    # 高橋君が投げたボールが消える距離を計算
    disappear_distance = V * S
    # 高橋君が投げたボールが消える時間と距離を比較
    if D < disappear_time or D > disappear_distance:
        print('Yes')
    else:
        print('No')
