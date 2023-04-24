Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    S, W = map(int, input().split())
    if S <= W:
        print("unsafe")
    else:
        print("safe")

=======
Suggestion 2

def main():
    s, w = map(int, input().split())
    if s <= w:
        print("unsafe")
    else:
        print("safe")

=======
Suggestion 3

def main():
    s, w = map(int, input().split())
    if s <= w:
        print('unsafe')
    else:
        print('safe')

=======
Suggestion 4

def main():
    # 入力
    S, W = map(int, input().split())
    # 出力
    if S <= W:
        print("unsafe")
    else:
        print("safe")

=======
Suggestion 5

def main():
    #input
    S, W = map(int, input().split())
    
    #output
    if W >= S:
        print("unsafe")
    else:
        print("safe")

=======
Suggestion 6

def main():
    # 入力を受け取る
    s, w = map(int, input().split())

    # 狼の数が羊の数以上なら unsafe
    if s <= w:
        print("unsafe")
    else:
        print("safe")
