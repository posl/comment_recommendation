Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    AB = []
    for i in range(N):
        AB.append(list(map(int, input().split())))
    AB.sort(key=lambda x: x[0] + x[1], reverse=True)
    Aoki = 0
    Takahashi = 0
    for i in range(N):
        if i % 2 == 0:
            Takahashi += AB[i][0] + AB[i][1]
        else:
            Aoki += AB[i][0]
    if Takahashi > Aoki:
        print(N)
    else:
        for i in range(N):
            Takahashi -= AB[i][0] + AB[i][1]
            Aoki += AB[i][0] + AB[i][1]
            if Takahashi > Aoki:
                print(i + 1)
                break

=======
Suggestion 2

def main():
    N = int(input())
    AB = [list(map(int, input().split())) for _ in range(N)]
    AB.sort(key=lambda x: x[0]+x[1], reverse=True)
    takahashi = 0
    aoki = 0
    for i in range(N):
        if i%2 == 0:
            takahashi += AB[i][0] + AB[i][1]
        else:
            aoki += AB[i][0]
    if takahashi > aoki:
        print(N)
    else:
        for i in range(N):
            if i%2 == 1:
                takahashi += AB[i][0] + AB[i][1]
                aoki -= AB[i][0]
            else:
                takahashi -= AB[i][0] + AB[i][1]
                aoki += AB[i][0]
            if takahashi > aoki:
                print(i+1)
                break

=======
Suggestion 3

def main():
    N = int(input())
    AB = [list(map(int, input().split())) for _ in range(N)]
    AB.sort(key=lambda x: x[0]+x[1], reverse=True)
    takahashi = 0
    aoki = 0
    for i in range(N):
        aoki += AB[i][0]
    for i in range(N):
        takahashi += AB[i][1]
        aoki -= AB[i][0]
        if takahashi > aoki:
            print(i+1)
            return

=======
Suggestion 4

def main():
    N = int(input())
    AB = [list(map(int, input().split())) for _ in range(N)]
    AB.sort(key=lambda x: x[0]+x[1], reverse=True)
    takahashi = 0
    aoki = 0
    for i in range(N):
        aoki += AB[i][0]
    for i in range(N):
        takahashi += AB[i][1]
        aoki -= AB[i][0]
        if takahashi > aoki:
            print(i+1)
            break

=======
Suggestion 5

def main():
    N = int(input())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)

    ans = 0
    Aoki = 0
    Takahashi = 0
    for i in range(N):
        Aoki += A[i]
        Takahashi += B[i]
        if A[i] + B[i] > max(Aoki, Takahashi):
            ans += 1

    print(ans)

=======
Suggestion 6

def main():
    N = int(input())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    diff = [A[i] + B[i] for i in range(N)]
    diff.sort(reverse=True)
    takahashi = 0
    aoki = 0
    for i in range(N):
        if i % 2 == 0:
            takahashi += diff[i]
        else:
            aoki += diff[i]
    if takahashi > aoki:
        print(N)
    else:
        for i in range(N):
            if takahashi - diff[i] + A[i] > aoki - B[i]:
                print(i + 1)
                break

=======
Suggestion 7

def main():
    N = int(input())
    AB = []
    for i in range(N):
        A, B = map(int, input().split())
        AB.append([A, B])
    AB.sort(key=lambda x: x[0]+x[1], reverse=True)
    takahashi = 0
    aoki = 0
    for i in range(N):
        if takahashi < aoki:
            takahashi += AB[i][0]
            aoki += AB[i][1]
        else:
            takahashi += AB[i][1]
            aoki += AB[i][0]
    if takahashi < aoki:
        print(N)
    else:
        print(N-1)

=======
Suggestion 8

def main():
    n = int(input())
    ab = []
    for i in range(n):
        a, b = map(int, input().split())
        ab.append((a, b))
    ab.sort(key=lambda x: x[0]+x[1], reverse=True)
    takahashi = 0
    aoki = 0
    for i in range(n):
        if i % 2 == 0:
            takahashi += ab[i][0]
        else:
            aoki += ab[i][1]
    if takahashi > aoki:
        print(0)
        return
    else:
        for i in range(n):
            if i % 2 == 0:
                takahashi += ab[i][1] - ab[i][0]
            else:
                aoki += ab[i][0] - ab[i][1]
            if takahashi > aoki:
                print(i+1)
                return

=======
Suggestion 9

def main():
    N = int(input())
    AB = [list(map(int, input().split())) for _ in range(N)]
    AB.sort(key = lambda x: x[0] + x[1], reverse=True)
    Aoki = 0
    Takahashi = 0
    for i in range(N):
        Takahashi += AB[i][1]
    for i in range(N):
        Takahashi -= AB[i][1]
        Aoki += AB[i][0]
        if Takahashi < Aoki:
            print(i + 1)
            return

=======
Suggestion 10

def main():
    #入力
    N = int(input())
    AB = [list(map(int, input().split())) for _ in range(N)]
    #ABの中のBの値を小さい順にソートする
    AB.sort(key=lambda x:x[1], reverse=True)
    #print(AB)
    #Aの合計値
    Asum = 0
    #Bの合計値
    Bsum = 0
    #Bの合計値とAの合計値を比較して、Aの合計値が大きくなるまで
    #Bの合計値をAの合計値に足していく
    for i in range(N):
        Bsum += AB[i][1]
        Asum += AB[i][0]
        if Asum > Bsum:
            break
    print(i+1)
