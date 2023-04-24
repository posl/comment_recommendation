Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    P = list(map(int, input().split()))
    cnt = 1
    min = P[0]
    for i in range(1, N):
        if min >= P[i]:
            cnt += 1
            min = P[i]
    print(cnt)

=======
Suggestion 2

def main():
    n = int(input())
    p = list(map(int,input().split()))
    count = 1
    min_p = p[0]
    for i in range(1,n):
        if p[i] <= min_p:
            min_p = p[i]
            count += 1
    print(count)

=======
Suggestion 3

def main():
    N = int(input())
    P = list(map(int, input().split()))
    ans = 0
    min_P = P[0]
    for i in range(1, N):
        if P[i] <= min_P:
            ans += 1
            min_P = P[i]
    ans += 1
    print(ans)

=======
Suggestion 4

def main():
    n = int(input())
    p = list(map(int, input().split()))
    ans = 0
    min_p = 10**6
    for i in range(n):
        if p[i] <= min_p:
            ans += 1
            min_p = p[i]
    print(ans)

=======
Suggestion 5

def main():
    N = int(input())
    P = list(map(int, input().split()))
    ans = 0
    minP = 10 ** 9 + 1
    for i in range(N):
        if P[i] <= minP:
            ans += 1
            minP = P[i]
    print(ans)

=======
Suggestion 6

def main():
    N = int(input())
    P = list(map(int,input().split()))
    #print(N)
    #print(P)
    #print(P[0])
    #print(P[1])
    #print(P[2])
    #print(P[3])
    #print(P[4])
    #print(P[5])
    #print(P[6])
    #print(P[7])
    
    #P[i] <= P[j] となる i,j の組み合わせをカウントする。
    #P[i] == P[j] の場合は、i < j となるもののみカウントする。
    #P[i] > P[j] の場合は、カウントしない。
    #i = 0 は除外する。
    #P[i] の最小値を求める。
    #P[i] の最小値が P[0] と等しい場合は、カウントしない。
    #P[i] の最小値が P[0] と等しくない場合は、カウントする。
    #P[i] の最小値が P[0] と等しくない場合は、P[i] の最小値が P[0] と等しい場合は、カウントしない。
    #P[i] の最小値が P[0] と等しい場合は、カウントする。
    #P[i] の最小値が P[0] と等しい場合は、P[i] の最小値が P[0] と等しい場合は、カウントする。
    #P[i] の最小値が P[0] と等しくない場合は、P[i] の最小値が P[0] と等しい場合は、カウントしない。
    #P[i] の最小値が P[0] と等しい場合は、カウントする。
    #P[i] の最小値が P[0] と等しい場合は、P[i] の

=======
Suggestion 7

def main():
    N = int(input())
    P = list(map(int, input().split()))
    #print(N)
    #print(P)
    count = 0
    for i in range(N):
        if P[i] == i + 1:
            count += 1
    print(count)

=======
Suggestion 8

def main():
    #入力
    N = int(input())
    P = list(map(int,input().split()))
    #処理
    ans = 0
    mi = P[0]
    for i in range(1,N):
        if mi >= P[i]:
            ans += 1
        mi = min(mi,P[i])
    ans += 1
    #出力
    print(ans)

main()

=======
Suggestion 9

def main():
    N = int(input())
    P = list(map(int, input().split()))

    # Pの最小値を求める
    min_P = P[0]
    for i in range(1, N):
        if P[i] < min_P:
            min_P = P[i]

    # Pの最小値を含む連続した部分列の長さを求める
    count = 1
    for i in range(1, N):
        if P[i] < min_P:
            break
        else:
            count += 1

    # Pの最小値を含む連続した部分列の長さを出力する
    print(count)

=======
Suggestion 10

def main():
    #N
    N = int(input())

    #P_1 ... P_N
    P = list(map(int, input().split()))

    #P_i ≦ P_j
    #i(1 ≦ i ≦ N) の個数
    count = 0

    #任意の整数 j(1 ≦ j ≦ i) に対して、 P_i ≦ P_j
    #i=1,2,3,4,...,N
    for i in range(N):
        #j=1,2,3,4,...,i
        for j in range(i+1):
            #P_i ≦ P_j
            if P[i] <= P[j]:
                #i(1 ≦ i ≦ N) の個数
                count += 1
                break

    #条件を満たす整数 i の個数
    print(count)
