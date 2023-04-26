Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    A, B, C = map(int, input().split())
    ans = -1
    for i in range(A, B+1):
        if i % C == 0:
            ans = i
            break
    print(ans)

=======
Suggestion 2

def main():
    A, B, C = map(int, input().split())
    for i in range(A, B+1):
        if i % C == 0:
            print(i)
            break
    else:
        print(-1)

=======
Suggestion 3

def main():
    A, B, C = map(int, input().split())
    for i in range(A, B+1):
        if i % C == 0:
            print(i)
            return
    print(-1)

=======
Suggestion 4

def main():
    a, b, c = map(int, input().split())
    for i in range(a, b+1):
        if i % c == 0:
            print(i)
            exit()
    print(-1)

=======
Suggestion 5

def main():
    A, B, C = input().split()
    A = int(A)
    B = int(B)
    C = int(C)
    for i in range(A, B+1):
        if i % C == 0:
            print(i)
            return
    print(-1)

=======
Suggestion 6

def main():
    # A,B,Cの入力
    A,B,C = map(int,input().split())
    # Cの倍数を格納するリスト
    C_multiple = []
    # Cの倍数をリストに格納
    for i in range(A,B+1):
        if i % C == 0:
            C_multiple.append(i)
    # Cの倍数がない場合
    if len(C_multiple) == 0:
        print(-1)
    # Cの倍数がある場合
    else:
        print(C_multiple[0])
