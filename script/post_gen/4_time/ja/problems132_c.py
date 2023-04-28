Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n = int(input())
    d = list(map(int, input().split()))
    d.sort()
    print(d[n//2]-d[n//2-1])

=======
Suggestion 2

def main():
    N = int(input())
    d = list(map(int, input().split()))
    d.sort()
    print(d[N//2]-d[N//2-1])

=======
Suggestion 3

def main():
    N = int(input())
    d = list(map(int, input().split()))
    d.sort()
    print(d[int(N/2)]-d[int(N/2)-1])

=======
Suggestion 4

def main():
    N = int(input())
    d = list(map(int, input().split()))
    d.sort()
    half = int(N/2)
    print(d[half] - d[half-1])

=======
Suggestion 5

def main():

    N = int(input())
    d = list(map(int, input().split()))
    d.sort()
    print(d[N//2] - d[N//2-1])

main()

=======
Suggestion 6

def main():
    N = int(input())
    d = list(map(int, input().split()))
    d.sort()
    #print(d)
    #print(N)

    if N%2 == 0:
        #偶数
        #print("even")
        #print(d[N//2-1])
        #print(d[N//2])
        ans = d[N//2] - d[N//2-1]
        print(ans)
    else:
        #奇数
        #print("odd")
        print(0)

=======
Suggestion 7

def main():
    N = int(input())
    D = list(map(int, input().split()))

    D.sort()
    #print(D)

    # Kを決めると、K以上の数がARC用の問題となる
    # K未満の数がABC用の問題となる
    # Kを決めるとABC用の問題の数は、K以上の数の個数となる
    # Kを決めるとARC用の問題の数は、K未満の数の個数となる
    # Kを決めるとARC用の問題の数とABC用の問題の数が同じになるとは、
    # K以上の数の個数とK未満の数の個数が同じになるということ

    # ARC用の問題の数を求める
    arc_count = 0
    for i in range(N):
        if D[i] >= D[N//2]:
            arc_count += 1

    # ABC用の問題の数を求める
    abc_count = 0
    for i in range(N):
        if D[i] < D[N//2]:
            abc_count += 1

    # ARC用の問題の数とABC用の問題の数が同じになるKの個数を求める
    if arc_count == abc_count:
        print(0)
    else:
        print(D[N//2] - D[N//2-1])
