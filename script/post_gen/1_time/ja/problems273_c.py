Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    a = list(map(int, input().split()))
    d = {}
    for i in range(n):
        if a[i] in d:
            d[a[i]] += 1
        else:
            d[a[i]] = 1
    d = sorted(d.items(), key=lambda x: x[0], reverse=True)
    #print(d)
    num = 0
    for i in range(len(d)):
        num += d[i][1]
        d[i] = (d[i][0], num)
    #print(d)
    ans = []
    for i in range(n):
        l = -1
        r = len(d)
        while r - l > 1:
            c = (l + r) // 2
            if d[c][0] > a[i]:
                l = c
            else:
                r = c
        #print(r)
        if r == len(d):
            ans.append(0)
        else:
            ans.append(d[r][1] - i - 1)
    for i in range(n):
        print(ans[i])

=======
Suggestion 2

def main():
    N = int(input())
    A = list(map(int, input().split()))
    # A = [2, 7, 1, 8, 2, 8]
    # N = 6
    # print(A)
    # print(N)
    A.sort()
    # print(A)
    # print(N)
    # print(A)

=======
Suggestion 3

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    A.append(0)
    cnt = 1
    ans = []
    for i in range(N):
        if A[i] == A[i+1]:
            cnt += 1
        else:
            ans.append(cnt)
            cnt = 1
    ans.append(0)
    ans.append(0)
    for i in range(1, N+1):
        ans[N-i] += ans[N-i+1]
        print(ans[N-i] - ans[i+1])

=======
Suggestion 4

def main():
    N = int(input())
    A = list(map(int, input().split()))

    A.sort()
    A.append(0)

    count = 0
    for i in range(N):
        if A[i] != A[i+1]:
            count += 1
        print(count - (N - i - 1))

=======
Suggestion 5

def main():
    N = int(input())
    A = [int(i) for i in input().split()]
    A = sorted(A, reverse=True)
    #print(A)
    for i in range(N):
        if i == 0:
            print(N)
        else:
            if A[i-1] == A[i]:
                continue
            else:
                print(N-i)

=======
Suggestion 6

def main():
    #入力
    N = int(input())
    A = list(map(int, input().split()))
    #Aの要素の種類数をカウント
    kind = len(set(A))
    #Aの要素の種類数をカウントするための辞書
    d = {}
    for i in range(N):
        d[A[i]] = 0
    #Aの要素の種類数をカウント
    for i in range(N):
        d[A[i]] += 1
    #Aの要素の種類数をカウントするための辞書
    d2 = {}
    for i in range(N):
        d2[A[i]] = 0
    #Aの要素の種類数をカウント
    for i in range(N):
        d2[A[i]] += 1
    #Aの要素の種類数をカウントするための辞書
    d3 = {}
    for i in range(N):
        d3[A[i]] = 0
    #Aの要素の種類数をカウント
    for i in range(N):
        d3[A[i]] += 1
    #Aの要素の種類数をカウントするための辞書
    d4 = {}
    for i in range(N):
        d4[A[i]] = 0
    #Aの要素の種類数をカウント
    for i in range(N):
        d4[A[i]] += 1
    #Aの要素の種類数をカウントするための辞書
    d5 = {}
    for i in range(N):
        d5[A[i]] = 0
    #Aの要素の種類数をカウント
    for i in range(N):
        d5[A[i]] += 1
    #Aの要素の種類数をカウントするための辞書
    d6 = {}
    for i in range(N):
        d6[A[i]] = 0
    #A

=======
Suggestion 7

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A = sorted(A)
    num = 1
    ans = []
    for i in range(N):
        if A[i] == A[i-1]:
            num += 1
        else:
            ans.append(num)
            num = 1
    ans.appen

=======
Suggestion 8

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    #print(A)
    #print(len(A))
    for i in range(N):
        #print(i)
        #print(A[i])
        #print(A[i+1:])
        #print(len(set(A[i+1:])))
        if len(A) == 1:
            print(1)
        elif i == N-1:
            print(0)
        elif A[i] == A[i+1]:
            print(1)
        else:
            print(len(set(A[i+1:])))

=======
Suggestion 9

def main():
    N = int(input())
    A = [int(i) for i in input().split()]
    #Aの種類の数を求める
    A_set = set(A)
    #Aの種類の数がKのときのiの個数を求める
    for i in range(1,N+1):
        #Aの種類の数がiのときのAの種類の数を求める
        A_i = A_set.pop()
        #Aの種類の数がiのときのAの種類の数がKのときのiの個数を求める
        count = 0
        for j in range(N):
            if A[j] > A_i:
                count += 1
                if count == i:
                    print(j+1)
                    break
        else:
            print(0)

=======
Suggestion 10

def main():
    N = int(input())
    A = list(map(int,input().split()))
    A.sort()

    #Aの値ごとに個数を数える
    count = []
    for i in range(N):
        if i == 0:
            count.append(1)
        elif A[i] == A[i-1]:
            count[-1] += 1
        else:
            count.append(1)

    #Aの値ごとに個数を数える
    count = []
    for i in range(N):
        if i == 0:
            count.append(1)
        elif A[i] == A[i-1]:
            count[-1] += 1
        else:
            count.append(1)

    #countを累積和の形にする
    count_sum = [0]
    for i in range(len(count)):
        count_sum.append(count_sum[i]+count[i])

    #Aの値ごとに個数を数える
    count = []
    for i in range(N):
        if i == 0:
            count.append(1)
        elif A[i] == A[i-1]:
            count[-1] += 1
        else:
            count.append(1)

    #countを累積和の形にする
    count_sum = [0]
    for i in range(len(count)):
        count_sum.append(count_sum[i]+count[i])

    #count_sumを累積和の形にする
    count_sum_sum = [0]
    for i in range(len(count_sum)):
        count_sum_sum.append(count_sum_sum[i]+count_sum[i])

    #Aの値ごとに個数を数える
    count = []
    for i in range(N):
        if i == 0:
            count.append(1)
        elif A[i] == A[i-1]:
            count[-1] += 1
        else:
            count.append(1)

    #countを累積和の形にする
    count_sum = [0]
    for i in range(len(count)):
        count_sum.append(count_sum[i]+count[i])

    #count_sumを累積和の形にする
    count_sum_sum = [0]
    for i in range(len(count_sum)):
