Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    a = list(map(int, input().split()))
    k = 0
    for i in range(3):
        k = a[k]
    print(k)

=======
Suggestion 2

def main():
    a = list(map(int, input().split()))
    ans = 0
    for i in range(3):
        ans = a[ans]
    print(ans)

=======
Suggestion 3

def main():
    a = list(map(int,input().split()))
    s = 0
    for i in range(3):
        s = a[s]
    print(s)

=======
Suggestion 4

def main():
    a = input().split()
    for i in range(3):
        a[0] = a[int(a[0])]
    print(a[0])

=======
Suggestion 5

def main():
    #入力
    a = list(map(int,input().split()))
    #処理
    for i in range(3):
        a0 = a[0]
        for j in range(9):
            a[j] = a[j+1]
        a[9] = a0
    #出力
    print(a[0])
    return

=======
Suggestion 6

def main():
    a = list(map(int, input().split()))
    print(a[a[0]])

=======
Suggestion 7

def main():
    a = list(map(int,input().split()))
    print(a[0])
