Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    D, T, S = map(int, input().split())
    if D / S <= T:
        print("Yes")
    else:
        print("No")

=======
Suggestion 2

def main():
    d, t, s = map(int, input().split())
    if d / s <= t:
        print("Yes")
    else:
        print("No")

=======
Suggestion 3

def main():
    D, T, S = map(int, input().split())
    if D / S <= T:
        print('Yes')
    else:
        print('No')

=======
Suggestion 4

def main():
    d, t, s = map(int, input().split())
    if d <= t * s:
        print("Yes")
    else:
        print("No")

=======
Suggestion 5

def main():
    D, T, S = map(int, input().split())
    if D <= T * S:
        print('Yes')
    else:
        print('No')

=======
Suggestion 6

def main():
    d, t, s = map(int, input().split())
    if d <= t * s:
        print('Yes')
    else:
        print('No')

=======
Suggestion 7

def main():
    d, t, s = map(int, input().split())
    if t * s >= d:
        print('Yes')
    else:
        print('No')

=======
Suggestion 8

def main():
    #標準入力から1行取得し、split()で分割し、map()でint型に変換し、リストに格納
    D,T,S = map(int, input().split())
    #待ち合わせ時刻までの距離を分速で割った値が待ち合わせ時刻以下であればYes
    if D/S <= T:
        print("Yes")
    else:
        print("No")
