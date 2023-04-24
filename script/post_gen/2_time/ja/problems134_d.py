Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    a = list(map(int, input().split()))
    if N == 1:
        if a[0] == 0:
            print(1)
            print(1)
        else:
            print(-1)
    elif N == 2:
        if a[0] == 0 and a[1] == 0:
            print(2)
            print(1, 2)
        elif a[0] == 1 and a[1] == 0:
            print(1)
            print(2)
        elif a[0] == 0 and a[1] == 1:
            print(1)
            print(1)
        else:
            print(-1)
    else:
        if a[0] == 1 and a[1] == 1 and a[2] == 1:
            print(-1)
        elif a[0] == 0 and a[1] == 1 and a[2] == 1:
            print(1)
            print(1)
        elif a[0] == 1 and a[1] == 0 and a[2] == 1:
            print(1)
            print(2)
        elif a[0] == 1 and a[1] == 1 and a[2] == 0:
            print(1)
            print(3)
        elif a[0] == 0 and a[1] == 0 and a[2] == 1:
            print(2)
            print(1, 2)
        elif a[0] == 0 and a[1] == 1 and a[2] == 0:
            print(2)
            print(1, 3)
        elif a[0] == 1 and a[1] == 0 and a[2] == 0:
            print(2)
            print(2, 3)
        elif a[0] == 0 and a[1] == 0 and a[2] == 0:
            print(3)
            print(1, 2, 3)
        else:
            print(-1)

=======
Suggestion 2

def main():
    N = int(input())
    a = list(map(int, input().split()))
    if a[0] == 1:
        print(-1)
        return
    if N == 1:
        print(0)
        return
    if N == 2:
        if a[1] == 1:
            print(-1)
        else:
            print(0)
        return
    ans = []
    for i in range(1, N):
        if a[i] == 1:
            ans.append(i)
            ans.append(i)
            ans.append(i - 1)
    print(len(ans))
    for i in ans:
        print(i, end=" ")
    print()

=======
Suggestion 3

def main():
    N = int(input())
    a = list(map(int, input().split()))
    if a[0] == 1:
        print(-1)
        return
    if N == 1:
        print(0)
        return
    if a[1] == 1:
        print(-1)
        return
    if N == 2:
        print(0)
        return
    if a[2] == 1:
        print(-1)
        return
    if N == 3:
        print(0)
        return
    #3以上
    for i in range(3, N):
        if a[i] == 1:
            if a[i-1] == 0 and a[i-2] == 0 and a[i-3] == 0:
                print(-1)
                return
    #print(a)
    ans = []
    for i in range(N):
        if a[i] == 1:
            ans.append(i+1)
    print(len(ans))
    print(*ans)

=======
Suggestion 4

def main():
    N = int(input())
    A = list(map(int, input().split()))
    if A[0] == 1:
        print(-1)
        return
    if N == 1:
        print(0)
        return
    if A[1] == 1:
        print(-1)
        return
    if N == 2:
        print(0)
        return
    if A[2] == 1:
        print(-1)
        return
    if N == 3:
        print(0)
        return
    if A[3] == 1:
        print(-1)
        return
    if N == 4:
        print(0)
        return
    if A[4] == 1:
        print(-1)
        return
    if N == 5:
        print(0)
        return
    if A[5] == 1:
        print(-1)
        return
    if N == 6:
        print(0)
        return
    if A[6] == 1:
        print(-1)
        return
    if N == 7:
        print(0)
        return
    if A[7] == 1:
        print(-1)
        return
    if N == 8:
        print(0)
        return
    if A[8] == 1:
        print(-1)
        return
    if N == 9:
        print(0)
        return
    if A[9] == 1:
        print(-1)
        return
    if N == 10:
        print(0)
        return
    if A[10] == 1:
        print(-1)
        return
    if N == 11:
        print(0)
        return
    if A[11] == 1:
        print(-1)
        return
    if N == 12:
        print(0)
        return
    if A[12] == 1:
        print(-1)
        return
    if N == 13:
        print(0)
        return
    if A[13] == 1:
        print(-1)
        return
    if N == 14:
        print(0)
        return
    if A[14] == 1:
        print(-1)
        return

=======
Suggestion 5

def main():
    n = int(input())
    a = [int(x) for x in input().split()]
    if a[0] == 1:
        print(-1)
        return
    if n == 1:
        print(0)
        return
    if a[1] == 1:
        print(-1)
        return
    if n == 2:
        print(0)
        return
    if a[2] == 1:
        print(-1)
        return

    ans = []
    for i in range(3, n):
        if a[i] == 1:
            ans.append(i+1)
    print(len(ans))
    print(' '.join(map(str, ans)))

=======
Suggestion 6

def main():
    N = int(input())
    a = list(map(int, input().split()))
    ans = []
    for i in range(N):
        if a[i] == 1:
            ans.append(i+1)
    if len(ans) % 2 == 0:
        print(len(ans))
        print(*ans)
    else:
        print(-1)

=======
Suggestion 7

def main():
    N = int(input())
    A = list(map(int,input().split()))
    B = []
    for i in range(N):
        if A[i] == 1:
            B.append(i+1)
    if len(B)%2 == 0:
        print(len(B))
        for i in range(len(B)):
            print(B[i])
    else:
        print(-1)

=======
Suggestion 8

def main():
    # 入力
    N = int(input())
    a = list(map(int, input().split()))

    # 処理
    ans = []
    for i in range(N):
        if a[i] == 1:
            ans.append(i+1)
            for j in range(2, N//(i+1)+1):
                a[j*(i+1)-1] = 1 - a[j*(i+1)-1]

    # 出力
    if sum(a) == 0:
        print(len(ans))
        print(*ans)
    else:
        print(-1)

=======
Suggestion 9

def solve(N, A):
    # 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,165,166,167,168,169,170,171,172,173,174,175,176,177,178,179,180,181,182,183,184,185,186,187,188,189,190,191,192,193,194,195,196,197,198,199,200,201,202,203,204,205,206,207,208,209,210,211,212,213,214,215,216,217,218,219,220,221,222,223,224,225,226,227,228,229,230,231,232,233,234,235,236,237,238,239,240,241,242,243,244,245,246,

=======
Suggestion 10

def main():
    N = int(input())
    A = list(map(int, input().split()))

    #2で割った余りが0の箱をリストに格納
    zero_box = []
    for i in range(N):
        if A[i] == 0:
            zero_box.append(i+1)

    #2で割った余りが1の箱をリストに格納
    one_box = []
    for i in range(N):
        if A[i] == 1:
            one_box.append(i+1)

    #2で割った余りが0の箱の個数と1の箱の個数の差が1以上なら-1を出力
    if abs(len(zero_box) - len(one_box)) >= 2:
        print(-1)
        exit()

    #2で割った余りが0の箱の個数が1多い場合
    if len(zero_box) - len(one_box) == 1:
        print(len(zero_box))
        for i in range(len(zero_box)):
            print(zero_box[i])

    #2で割った余りが1の箱の個数が1多い場合
    elif len(zero_box) - len(one_box) == -1:
        print(len(one_box))
        for i in range(len(one_box)):
            print(one_box[i])

    #2で割った余りが0の箱の個数と1の箱の個数が同じ場合
    else:
        print(len(zero_box))
        for i in range(len(zero_box)):
            print(zero_box[i])
