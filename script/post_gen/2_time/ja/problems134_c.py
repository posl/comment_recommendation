Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    A = []
    for i in range(N):
        A.append(int(input()))
    max1 = max(A)
    A.remove(max1)
    max2 = max(A)
    for i in range(N):
        if A[i] == max1:
            print(max2)
        else:
            print(max1)

=======
Suggestion 2

def main():
    N = int(input())
    A = [int(input()) for _ in range(N)]
    maxA = max(A)
    for i in range(N):
        if A[i] == maxA:
            A[i] = 0
    maxA = max(A)
    for i in range(N):
        print(maxA)

=======
Suggestion 3

def main():
    n = int(input())
    a = [int(input()) for _ in range(n)]
    a.sort()
    max1 = a[-1]
    max2 = a[-2]
    for i in range(n):
        if a[i] == max1:
            print(max2)
        else:
            print(max1)

=======
Suggestion 4

def main():
    N = int(input())
    A = []
    for i in range(N):
        A.append(int(input()))

    maxA = max(A)
    maxA_index = A.index(maxA)

    for i in range(N):
        if i == maxA_index:
            A.remove(maxA)
            print(max(A))
            A.insert(maxA_index, maxA)
        else:
            print(maxA)

=======
Suggestion 5

def main():
    N = int(input())
    A = [int(input()) for _ in range(N)]
    max_a = max(A)
    max_a_idx = A.index(max_a)
    A.pop(max_a_idx)
    max_a2 = max(A)
    for i in range(N):
        if i == max_a_idx:
            print(max_a2)
        else:
            print(max_a)

=======
Suggestion 6

def main():
    N = int(input())
    A = [int(input()) for _ in range(N)]
    A_max = max(A)
    A_max_idx = A.index(A_max)
    A2 = A.copy()
    A2.pop(A_max_idx)
    A2_max = max(A2)
    for i in range(N):
        if i == A_max_idx:
            print(A2_max)
        else:
            print(A_max)

=======
Suggestion 7

def main():
    N = int(input())
    A = [int(input()) for _ in range(N)]

    # 1つ目の最大値を求める
    max1 = 0
    for i in range(N):
        if A[i] > max1:
            max1 = A[i]
            max1_index = i

    # 2つ目の最大値を求める
    max2 = 0
    for i in range(N):
        if i == max1_index:
            continue
        if A[i] > max2:
            max2 = A[i]

    # 出力
    for i in range(N):
        if i == max1_index:
            print(max2)
        else:
            print(max1)

=======
Suggestion 8

def main():
    N = int(input())
    A = [int(input()) for _ in range(N)]
    #Aを降順にソート
    A.sort(reverse=True)
    #Aの最大値を求める
    max_A = A[0]
    #Aの2番目の最大値を求める
    second_max_A = A[1]
    
    for i in range(N):
        if A[i] == max_A:
            print(second_max_A)
        else:
            print(max_A)

=======
Suggestion 9

def main():
    N = int(input())
    A = [int(input()) for _ in range(N)]

    # 1. Aの最大値を取得する
    max_A = max(A)

    # 2. Aの最大値を除くAの最大値を取得する
    A.remove(max_A)
    max_A2 = max(A)

    # 3. Aの各要素を最大値と比較する
    for i in range(N):
        if A[i] == max_A:
            print(max_A2)
        else:
            print(max_A)

=======
Suggestion 10

def main():
    N = int(input())
    A = []
    for i in range(N):
        A.append(int(input()))

    # 最大値の個数
    max_num = 0
    # 最大値
    max_val = 0
    # 2番目に大きい値
    second_max_val = 0
    for i in range(N):
        if max_val < A[i]:
            max_val = A[i]
            max_num = 1
        elif max_val == A[i]:
            max_num += 1
        elif second_max_val < A[i]:
            second_max_val = A[i]

    for i in range(N):
        if A[i] == max_val and max_num == 1:
            print(second_max_val)
        else:
            print(max_val)
