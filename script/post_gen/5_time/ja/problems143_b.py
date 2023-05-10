Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = int(input())
    d = list(map(int, input().split()))
    sum = 0
    for i in range(N):
        for j in range(i+1, N):
            sum += d[i] * d[j]
    print(sum)

=======
Suggestion 2

def main():
    N = int(input())
    d = list(map(int, input().split()))
    sum = 0
    for i in range(N):
        for j in range(i+1,N):
            sum = sum + d[i] * d[j]
    print(sum)

=======
Suggestion 3

def sum_of_combination(num):
    sum = 0
    for i in range(num):
        for j in range(i+1,num):
            sum += d[i] * d[j]
    return sum

n = int(input())
d = list(map(int,input().split()))
print(sum_of_combination(n))

=======
Suggestion 4

def getSumOfTakoyakiPower(takoyakiPowerList):
    sumOfTakoyakiPower = 0
    for i in range(len(takoyakiPowerList)):
        for j in range(i+1,len(takoyakiPowerList)):
            sumOfTakoyakiPower = sumOfTakoyakiPower + takoyakiPowerList[i] * takoyakiPowerList[j]
    return sumOfTakoyakiPower

=======
Suggestion 5

def main():
    n = int(input())
    d = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        for j in range(i+1,n):
            ans += d[i] * d[j]
    print(ans)

=======
Suggestion 6

def solve():
    N = int(input())
    d = list(map(int, input().split()))

    # 2つ選ぶ方法はN*(N-1)/2通り
    # そのそれぞれについて、一緒に食べたときの体力の回復量を求める
    # その総和を出力する
    # 体力の回復量は、おいしさの積
    # おいしさの積を求めるのに、2重ループを回す
    # 2重ループの中で、おいしさの積を求めて、総和を取る
    # 2重ループの中で、おいしさの積を求めるには、
    # おいしさのリストをソートして、小さい順に取り出して、
    # おいしさの積を求める
    # おいしさのリストをソートするには、sorted を使う

    d_sorted = sorted(d)
    sum = 0
    for i in range(N):
        for j in range(i+1, N):
            sum += d_sorted[i] * d_sorted[j]

    print(sum)

=======
Suggestion 7

def main():
    n = int(input())
    d = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        for j in range(i+1, n):
            ans += d[i] * d[j]
    print(ans)
    return

=======
Suggestion 8

def main():
    n = int(input())
    d = list(map(int,input().split()))
    sum = 0
    for i in range(n-1):
        for j in range(i+1,n):
            sum += d[i]*d[j]
    print(sum)
