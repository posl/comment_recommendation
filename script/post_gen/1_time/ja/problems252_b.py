Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.sort(reverse=True)
    B.sort()
    if A[0] > B[0]:
        print("Yes")
    else:
        print("No")
    return

=======
Suggestion 2

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.sort(reverse=True)
    B.sort()
    for i in range(K):
        if A[i] < B[i]:
            print("Yes")
            exit()
    print("No")

=======
Suggestion 3

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    maxA = max(A)
    for i in range(K):
        if B[i] == A.index(maxA) + 1:
            print("Yes")
            return
    print("No")
    return

=======
Suggestion 4

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    maxA = max(A)
    for i in range(K):
        if B[i] == A.index(maxA) + 1:
            print('Yes')
            return
    print('No')

=======
Suggestion 5

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    print('Yes' if max(a) in a and max(a) not in b else 'No')

=======
Suggestion 6

def main():
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    a.sort(reverse=True)
    for i in range(k):
        if a[0] == a[b[i]-1]:
            print("Yes")
            return
    print("No")
    return

=======
Suggestion 7

def main():
    # 食品の数と嫌いな食品の数
    n, k = map(int, input().split())
    # 食品のおいしさ
    a = list(map(int, input().split()))
    # 嫌いな食品
    b = list(map(int, input().split()))
    # 食品のおいしさが最大の食品
    max_a = max(a)
    # 食品のおいしさが最大の食品のインデックス
    max_a_index = a.index(max_a)
    # 食品のおいしさが最大の食品のインデックスが嫌いな食品のリストに含まれるか
    if max_a_index + 1 in b:
        print('Yes')
    else:
        print('No')

=======
Suggestion 8

def main():
    #入力
    N, K = map(int, input().split()) #N個の食品 K個の嫌いな食品
    A = list(map(int, input().split())) #食品のおいしさ
    B = list(map(int, input().split())) #嫌いな食品番号

    #処理
    maxA = max(A) #おいしさが最大の食品のおいしさ
    if maxA in A: #おいしさが最大の食品があれば
        maxAindex = A.index(maxA) #おいしさが最大の食品の番号
        if maxAindex+1 in B: #嫌いな食品の番号と一致するなら
            print("Yes") #Yes
        else:
            print("No") #No
    else:
        print("No") #No

=======
Suggestion 9

def main():
    #入力
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    #処理
    a.sort()
    b.sort()
    if a[-1] > b[0]:
        print('Yes')
    else:
        print('No')

=======
Suggestion 10

def main():
    N, K = map(int, input().split())
    A = input().split()
    B = input().split()
    A.sort(reverse=True)
    B.sort(reverse=True)
    if A[0] <= B[0]:
        print("No")
    else:
        print("Yes")
