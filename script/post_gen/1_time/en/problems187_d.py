Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    A = [0] * N
    B = [0] * N
    for i in range(N):
        A[i], B[i] = map(int, input().split())
    A.sort(reverse=True)
    B.sort(reverse=True)
    Aoki = 0
    Takahashi = 0
    for i in range(N):
        Aoki += A[i]
        Takahashi += B[i]
        if Aoki < Takahashi:
            print(i + 1)
            return
    print(N)

=======
Suggestion 2

def main():
    N = int(input())
    AB = [list(map(int, input().split())) for _ in range(N)]
    AB = sorted(AB, key=lambda x: x[0] + x[1], reverse=True)
    diff = 0
    ans = 0
    for i in range(N):
        diff += AB[i][0]
        ans += 1
        if diff > sum(AB[i][1] for i in range(i+1, N)):
            break
    print(ans)

=======
Suggestion 3

def main():
    N = int(input())
    AB = []
    for i in range(N):
        AB.append(list(map(int, input().split())))
    AB.sort(key=lambda x: x[0] + x[1], reverse=True)
    ans = 0
    takahashi = 0
    aoki = 0
    for i in range(N):
        aoki += AB[i][0]
    for i in range(N):
        takahashi += AB[i][1]
        aoki -= AB[i][0]
        ans += 1
        if takahashi > aoki:
            break
    print(ans)

=======
Suggestion 4

def main():
    N = int(input())
    AB = [list(map(int, input().split())) for _ in range(N)]
    AB.sort(key=lambda x:x[0]+x[1], reverse=True)
    takahashi = 0
    aoki = 0
    for i in range(N):
        aoki += AB[i][0]
    ans = 0
    for i in range(N):
        takahashi += AB[i][1]
        aoki -= AB[i][0]
        ans += 1
        if takahashi > aoki:
            print(ans)
            return

=======
Suggestion 5

def main():
    N = int(input())
    A = []
    B = []
    for _ in range(N):
        a, b = map(int, input().split())
        A.append((a, b))
        B.append((b, a))
    A.sort(reverse=True)
    B.sort(reverse=True)
    aoki = 0
    takahashi = 0
    for i in range(N):
        aoki += A[i][0]
        takahashi += B[i][0]
        if aoki < takahashi:
            print(i+1)
            return

=======
Suggestion 6

def main():
    n = int(input())
    town = []
    for i in range(n):
        a, b = map(int, input().split())
        town.append([a, b])
    town = sorted(town, key=lambda x: x[0] + x[1], reverse=True)
    takahashi = 0
    aoki = 0
    result = 0
    for i in range(n):
        takahashi += town[i][0]
        aoki += town[i][1]
        result += 1
        if takahashi > aoki:
            break
    print(result)

=======
Suggestion 7

def main():
    n = int(input())
    a = []
    b = []
    for i in range(n):
        a_, b_ = map(int, input().split())
        a.append(a_)
        b.append(b_)

    a.sort(reverse = True)
    b.sort(reverse = True)

    #print(a)
    #print(b)

    takahashi = 0
    aoki = 0
    for i in range(n):
        #print("aoki = ", aoki)
        #print("takahashi = ", takahashi)
        if aoki >= takahashi:
            takahashi += b[i]
        else:
            aoki += a[i]
        #print("aoki = ", aoki)
        #print("takahashi = ", takahashi)
        if aoki > takahashi:
            print(i+1)
            exit()

main()

=======
Suggestion 8

def main():
    N = int(input())
    A, B = [], []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    #print(N, A, B)

    #Aokiの得票数が多い順にソート
    C = sorted([(A[i] + B[i], A[i], B[i]) for i in range(N)], reverse=True)
    #print(C)

    #TakahashiはAokiの得票数が多い順にスピーチを行う
    #Aokiの得票数が多い順にスピーチを行うと、
    #Aokiの得票数が多い順にスピーチを行った時の、
    #Takahashiの得票数が最大になる
    takahashi = 0
    aoki = 0
    for i in range(N):
        takahashi += C[i][1]
        aoki += C[i][2]
        if takahashi > aoki:
            print(i + 1)
            break

=======
Suggestion 9

def main():
    N = int(input())
    AB = [list(map(int, input().split())) for _ in range(N)]
    AB.sort(key=lambda x: -x[0]-x[1])
    aoki = 0
    takahashi = 0
    for i in range(N):
        aoki += AB[i][0]
    for i in range(N):
        takahashi += AB[i][1]
        aoki -= AB[i][0]
        if takahashi > aoki:
            print(i+1)
            return

=======
Suggestion 10

def main():
    N = int(input())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    
    #A[i] + B[i]の値を昇順に並び替える
    #A[i] + B[i]の値が同じ場合は、A[i]の値を昇順に並び替える
    #A[i] + B[i]の値が同じで、A[i]の値も同じ場合は、B[i]の値を昇順に並び替える
    #これらの値を元に、A[i] + B[i]の値が大きい順に並び替える
    #並び替え後のリストのインデックスを保持するリストを作成する
    #インデックスのリストの要素数をカウントする
    #インデックスのリストの要素数をカウントする
    #インデックスのリストの要素数と、A[i] + B[i]の値が大きい順に並び替える
    #インデックスのリストの要素数と、A[i] + B[i]の値が大きい順に並び替える
    #インデックスのリストの要素数と、A[i] + B[i]の値が大きい順に並び替える
    #インデックスのリストの要素数と、A[i] + B[i]の値が大きい順に並び替える
    #インデックスのリストの要素数と、A[i] + B[i]の値が大きい順に並び替える
    #インデックスのリストの要素数と、A[i] + B[i]の値が大
