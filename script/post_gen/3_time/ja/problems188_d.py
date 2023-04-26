Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, C = map(int, input().split())
    A = []
    B = []
    C = []
    for i in range(N):
        a, b, c = map(int, input().split())
        A.append(a)
        B.append(b)
        C.append(c)
    A.sort()
    B.sort()
    C.sort()
    #print(A)
    #print(B)
    #print(C)
    ans = 0
    for i in range(N):
        ans += A[i] * (N - i) + B[i] * (i + 1)
    print(ans)

=======
Suggestion 2

def main():
    N, C = map(int, input().split())
    AB = []
    for i in range(N):
        a, b, c = map(int, input().split())
        AB.append((a, c))
        AB.append((b+1, -c))

    AB.sort(key=lambda x: x[0])
    ans = 0
    cnt = 0
    for i in range(len(AB)-1):
        cnt += AB[i][1]
        ans += min(cnt, C) * (AB[i+1][0] - AB[i][0])

    print(ans)

=======
Suggestion 3

def main():
    N, C = map(int, input().split())
    A = []
    for i in range(N):
        a, b, c = map(int, input().split())
        A.append([a, c])
        A.append([b+1, -c])
    A.sort()
    ans = 0
    tmp = 0
    for i in range(len(A)):
        ans += min(C, tmp) * (A[i][0] - A[i-1][0])
        tmp += A[i][1]
    print(ans)

=======
Suggestion 4

def main():
    N, C = map(int, input().split())
    abc = [list(map(int, input().split())) for _ in range(N)]
    abc.sort(key=lambda x: x[1])
    ans = 0
    for i in range(N):
        a, b, c = abc[i]
        ans += c
        for j in range(i + 1, N):
            if abc[j][0] <= b:
                abc[j][0] = b + 1
            else:
                break
    abc.sort(key=lambda x: x[0])
    for i in range(N):
        a, b, c = abc[i]
        ans += min(C, c) * (b - a + 1)
    print(ans)

=======
Suggestion 5

def main():
    N, C = map(int, input().split())
    ABC = [list(map(int, input().split())) for _ in range(N)]
    ABC.sort(key=lambda x: x[0])
    #print(ABC)
    #print(C)
    #print(N)
    #print(ABC)
    #print(ABC[0])
    #print(ABC[1])
    #print(ABC[2])
    #print(ABC[3])
    #print(ABC[4])
    #print(ABC[0][0])
    #print(ABC[0][1])
    #print(ABC[0][2])
    #print(ABC[1][0])
    #print(ABC[1][1])
    #print(ABC[1][2])
    #print(ABC[2][0])
    #print(ABC[2][1])
    #print(ABC[2][2])
    #print(ABC[3][0])
    #print(ABC[3][1])
    #print(ABC[3][2])
    #print(ABC[4][0])
    #print(ABC[4][1])
    #print(ABC[4][2])
    #print(ABC[0][0] < ABC[1][0])
    #print(ABC[0][0] < ABC[2][0])
    #print(ABC[0][0] < ABC[3][0])
    #print(ABC[0][0] < ABC[4][0])
    #print(ABC[1][0] < ABC[2][0])
    #print(ABC[1][0] < ABC[3][0])
    #print(ABC[1][0] < ABC[4][0])
    #print(ABC[2][0] < ABC[3][0])
    #print(ABC[2][0] < ABC[4][0])
    #print(ABC[3][0] < ABC[4][0])
    #print(ABC[0][0] < ABC[1][0] < ABC[2][0] < ABC[3][0] < ABC[4][0])
    #print(ABC[0][1] < ABC[1][1] < ABC[2][1] < ABC[3][1] < ABC[4][1

=======
Suggestion 6

def main():
    N, C = map(int, input().split())
    ABC = [list(map(int, input().split())) for _ in range(N)]
    ABC.sort()

    # すぬけプライムに加入している期間
    # すぬけプライムに加入している期間に、別のサービスを利用している場合は、
    # その期間については、すぬけプライムに加入しているとみなす
    # すぬけプライムに加入している期間に、別のサービスを利用していない場合は、
    # その期間はすぬけプライムに加入していないとみなす
    # すぬけプライムに加入していない期間に、別のサービスを利用している場合は、
    # その期間はすぬけプライムに加入していないとみなす
    # すぬけプライムに加入していない期間に、別のサービスを利用していない場合は、
    # その期間については、すぬけプライムに加入しているとみなす
    # すぬけプライムに加入している期間は、
    # すぬけプライムに加入している期間に、別のサービスを利用している場合は、
    # その期間については、すぬけプライムに加入しているとみなす
    # すぬけプライムに加入していない期間に、別のサービスを利用している場合は、
    # その期間はすぬけプライムに加入していないとみなす
    # すぬけプラ

=======
Suggestion 7

def get_input():
    n, c = map(int, input().split())
    a = []
    b = []
    c = []
    for i in range(n):
        ai, bi, ci = map(int, input().split())
        a.append(ai)
        b.append(bi)
        c.append(ci)
    return n, c, a, b, c

=======
Suggestion 8

def main():
    N, C = map(int, input().split())
    ABC = [list(map(int, input().split())) for _ in range(N)]
    ABC.sort()
    #print(ABC)
    #print(N, C)
    total = 0
    prev = 0
    for i in range(N):
        #print(ABC[i])
        a, b, c = ABC[i]
        #print(a, b, c)
        if i == 0:
            total += (b - a + 1) * c
            prev = b
        else:
            if prev >= a:
                total += (b - prev) * c
                prev = b
            else:
                total += (b - a + 1) * c
                prev = b
    print(total + C)

=======
Suggestion 9

def main():
    N, C = map(int, input().split())
    abc = [list(map(int, input().split())) for _ in range(N)]

    # 1日目から最終日までのすぬけプライムの有無を格納するリスト
    # 1日目から最終日までのすぬけプライムの有無を格納するリスト
    dp = [0] * (10 ** 9 + 1)

    for i in range(N):
        a, b, c = abc[i]
        dp[a] += c
        dp[b + 1] -= c

    for i in range(1, 10 ** 9 + 1):
        dp[i] += dp[i - 1]

    ans = 0
    for i in range(1, 10 ** 9 + 1):
        ans += min(dp[i], C)

    print(ans)

=======
Suggestion 10

def main():
    N, C = map(int, input().split())
    # 1日目からN日目までのサービスの利用料金の最小値を求める
    # ある日の利用料金は、その日に利用するサービスの中で最小の料金になる
    # ある日に利用するサービスは、その日に利用が開始されるサービスと、
    # その日に利用が終了するサービスの両方に含まれる
    # ある日に利用するサービスの中で最小の料金は、
    # その日に利用が開始されるサービスの料金と、
    # その日に利用が終了するサービスの料金の両方に含まれる
    # ある日に利用が開始されるサービスの料金は、
    # その日に利用が開始されるサービスの開始日の前の1日の利用料金に、
    # その日に利用が開始されるサービスの料金を加えたものになる
    # ある日に利用が終了するサービスの料金は、
    # その日に利用が終了するサービスの終了日の後の1日の利用料金に、
    # その日に利用が終了するサービスの料金を加えたものになる
    # ある日に利用が開始されるサービスの開始日の前の1日の利用料金は、
    # その日に利用が開始されるサービスの開始日の前の1日の日付に、
    # その日に利用が開始されるサービスの料金を加えたものになる
    # ある日に
