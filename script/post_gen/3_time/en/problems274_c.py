Synthesizing 9/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = [0] * (2 * N + 1)
    for i in range(N):
        ans[A[i]] = 1
    for i in range(N):
        if ans[2 * A[i]] == 1:
            ans[2 * A[i] + 1] = ans[A[i]] + 1
        else:
            ans[2 * A[i]] = ans[A[i]] + 1
    print('

'.join(map(str, ans)))

=======
Suggestion 2

def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = [0] * (2 * N + 1)
    for i in range(N):
        ans[A[i]] = ans[A[i] // 2] + 1
        ans[A[i] + 1] = ans[A[i] // 2] + 1
    for i in range(2 * N + 1):
        print(ans[i])

=======
Suggestion 3

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.reverse()
    ans = [0] * (2 * n + 1)
    for i in range(n):
        ans[a[i] - 1] = ans[(a[i] - 1) // 2] + 1
    for i in range(2 * n + 1):
        print(ans[i])

=======
Suggestion 4

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A = [0] + A
    ans = [0] * (2 * N + 1)

    for i in range(1, N + 1):
        ans[A[i]] = ans[A[i] // 2] + 1

    for i in range(1, 2 * N + 1):
        print(ans[i])

=======
Suggestion 5

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A = [0] + A
    ans = [0] * (2**N + 1)
    for i in range(1, N+1):
        ans[A[i]] = ans[A[i]//2] + 1
    print(*ans[1:], sep='

')

=======
Suggestion 6

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a = [0] + a
    ans = [0] * (2 ** n + 1)
    for i in range(n):
        ans[a[i]] = ans[a[i] // 2] + 1
    for i in range(2 ** n + 1):
        print(ans[i])

=======
Suggestion 7

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a = a[::-1]
    ans = [0] * (2**n+1)
    for i in range(n):
        ans[a[i]] = ans[a[i]*2] + 1
        ans[a[i]*2+1] = ans[a[i]*2] + 1
    print(*ans[1:], sep='
')

=======
Suggestion 8

def main():
    N = int(input())
    A = list(map(int,input().split()))

    d = {1:0}
    for i in range(1,N+1):
        d[2*i] = d[A[i-1]] + 1
        d[2*i+1] = d[A[i-1]] + 1

    for i in range(2**N):
        print(d[i+1])

=======
Suggestion 9

def main():
    N = int(input())
    A = list(map(int, input().split()))
    # 2^40 = 1,099,511,627,776
    # 2^41 = 2,199,023,255,552
    # 2^42 = 4,398,046,511,104
    # 2^43 = 8,796,093,022,208
    # 2^44 = 17,592,186,044,416
    # 2^45 = 35,184,372,088,832
    # 2^46 = 70,368,744,177,664
    # 2^47 = 140,737,488,355,328
    # 2^48 = 281,474,976,710,656
    # 2^49 = 562,949,953,421,312
    # 2^50 = 1,125,899,906,842,624
    # 2^51 = 2,251,799,813,685,248
    # 2^52 = 4,503,599,627,370,496
    # 2^53 = 9,007,199,254,740,992
    # 2^54 = 18,014,398,509,481,984
    # 2^55 = 36,028,797,018,963,968
    # 2^56 = 72,057,594,037,927,936
    # 2^57 = 144,115,188,075,855,872
    # 2^58 = 288,230,376,151,711,744
    # 2^59 = 576,460,752,303,423,488
    # 2^60 = 1,152,921,504,606,846,976
    # 2^61 = 2,305,843,009,213,693,952
    # 2^62 = 4,611,686,018,427,387,904
    # 2^63 = 9,223,372,036,854,775,808
    # 2^64 = 18,446,744
