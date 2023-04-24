Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    T = int(input())
    for i in range(T):
        N = int(input())
        A = list(map(int,input().split()))
        count = 0
        for j in range(N):
            if A[j] % 2 != 0:
                count += 1
        print(count)

=======
Suggestion 2

def main():
    T = int(input())
    for i in range(T):
        N = int(input())
        A = list(map(int, input().split()))
        count = 0
        for j in range(N):
            if A[j]%2 == 1:
                count += 1
        print(count)

=======
Suggestion 3

def main():
    T = int(input())
    for i in range(T):
        N = int(input())
        A = list(map(int, input().split()))
        odd = 0
        for j in range(N):
            if A[j] % 2 == 1:
                odd += 1
        print(odd)

=======
Suggestion 4

def main():
    T = int(input())
    for i in range(T):
        N = int(input())
        A = list(map(int, input().split()))
        print(len(list(filter(lambda x: x % 2 == 1, A))))

=======
Suggestion 5

def main():
    T = int(input())
    for i in range(0,T):
        N = int(input())
        A = list(map(int,input().split()))
        count = 0
        for j in range(0,N):
            if A[j] % 2 == 1:
                count += 1
        print(count)

=======
Suggestion 6

def main():
    N = int(input())
    A = list(map(int, input().split()))
    print(len([i for i in A if i % 2 == 1]))

=======
Suggestion 7

def main():
    # 1行目の読み込み
    N = int(input())
    # 2行目の読み込み
    A = list(map(int, input().split()))
    # 奇数の個数をカウントする変数
    count = 0
    # 奇数の個数をカウントする
    for i in range(N):
        if A[i] % 2 != 0:
            count += 1
    print(count)

=======
Suggestion 8

def main():
    #T = int(input())
    T = 4
    #for i in range(T):
    #    N = int(input())
    #    A = list(map(int, input().split()))
    N = 3
    A = [1,2,3]
    N = 2
    A = [20,23]
    N = 10
    A = [6,10,4,1,5,9,8,6,5,1]
    N = 1
    A = [1000000000]
    count = 0
    for j in range(N):
        if A[j] % 2 != 0:
            count += 1
    print(count)

=======
Suggestion 9

def main():
    t = int(input()) #input()で標準入力から1行読み込み、int()で整数に変換
    for i in range(t):
        n = int(input())
        a = list(map(int,input().split()))
        odd = 0
        for j in range(n):
            if a[j]%2 != 0:
                odd += 1
        print(odd)
