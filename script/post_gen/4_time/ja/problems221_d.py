Synthesizing 1/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)

    #print(A)
    #print(B)

    # それぞれの日にちに何人いたかをカウントする
    # その日にちにログインした人数
    # その日にちの終わりにログアウトした人数
    # 終わりの日にちにログアウトした人数
    #print(A)
    #print(B)
    #print(list(map(lambda x:
