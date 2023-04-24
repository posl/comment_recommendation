Synthesizing 9/10 solutions

=======
Suggestion 1

def main():
    N, W = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    dp = [0] * (W + 1)
    dp[0] = 1
    for i in range(N):
        for j in range(W - A[i], -1, -1):
            if dp[j] > 0:
                dp[j + A[i]] += dp[j]
    print(sum(dp))

=======
Suggestion 2

def main():
    N, W = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    dp = [0] * (W+1)
    dp[0] = 1
    ans = 0
    for i in range(N):
        for j in range(W, A[i]-1, -1):
            dp[j] |= dp[j-A[i]]
        ans += dp.count(1)
    print(ans)

=======
Suggestion 3

def main():
    N,W = map(int,input().split())
    A = list(map(int,input().split()))
    A.sort()
    dp = [0] * (W+1)
    dp[0] = 1
    for i in A:
        for j in range(W,-1,-1):
            if dp[j] == 1 and j+i <= W:
                dp[j+i] = 1
    print(sum(dp))

=======
Suggestion 4

def main():
    N,W = map(int,input().split())
    A = list(map(int,input().split()))
    A.sort()
    #print(A)

=======
Suggestion 5

def main():
    N, W = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    c = 0
    for i in range(N):
        for j in range(i,N):
            for k in range(j,N):
                if A[i] + A[j] + A[k] <= W:
                    c += 1
    print(c)

=======
Suggestion 6

def main():
    N, W = map(int, input().split())
    A = list(map(int, input().split()))
    #print(N, W, A)

    # N = 2
    # W = 10
    # A = [1, 3]

    # N = 2
    # W = 1
    # A = [2, 3]

    # N = 4
    # W = 12
    # A = [3, 3, 3, 3]

    # N = 7
    # W = 251
    # A = [202, 20, 5, 1, 4, 2, 100]

    # N = 300
    # W = 10**6
    # A = [10**6] * N

    # N = 300
    # W = 10**6
    # A = [10**6 - i for i in range(N)]

    # N = 300
    # W = 10**6
    # A = [i for i in range(N)]

    # N = 300
    # W = 10**6
    # A = [10**6, 10**6]

    # N = 300
    # W = 10**6
    # A = [10**6 - i for i in range(N)] + [10**6]

    # N = 300
    # W = 10**6
    # A = [10**6 - i for i in range(N)] + [10**6 - 1]

    # N = 300
    # W = 10**6
    # A = [10**6 - i for i in range(N)] + [10**6 - 2]

    # N = 300
    # W = 10**6
    # A = [10**6 - i for i in range(N)] + [10**6 - 3]

    # N = 300
    # W = 10**6
    # A = [10**6 - i for i in range(N)] + [10**6 - 4]

    # N = 300
    # W = 10**6
    # A = [10**6 - i for i in

=======
Suggestion 7

def main():
    N, W = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    #print(A)
    #print(N, W)
    #print(A)
    #print(A[0])
    #print(A[1])
    #print(A[2])
    #print(A[3])
    #print(A[4])
    #print(A[5])
    #print(A[6])
    #print(A[7])
    #print(A[8])
    #print(A[9])
    #print(A[10])
    #print(A[11])
    #print(A[12])
    #print(A[13])
    #print(A[14])
    #print(A[15])
    #print(A[16])
    #print(A[17])
    #print(A[18])
    #print(A[19])
    #print(A[20])
    #print(A[21])
    #print(A[22])
    #print(A[23])
    #print(A[24])
    #print(A[25])
    #print(A[26])
    #print(A[27])
    #print(A[28])
    #print(A[29])
    #print(A[30])
    #print(A[31])
    #print(A[32])
    #print(A[33])
    #print(A[34])
    #print(A[35])
    #print(A[36])
    #print(A[37])
    #print(A[38])
    #print(A[39])
    #print(A[40])
    #print(A[41])
    #print(A[42])
    #print(A[43])
    #print(A[44])
    #print(A[45])
    #print(A[46])
    #print(A[47])
    #print(A[48])
    #print(A[49])
    #print(A[50])
    #print(A[51])
    #print(A[52])
    #print(A[53])
    #print(A[54])
    #print(A[55])
    #print(A[56])
    #print(A[57])
    #print(A[58])
    #print(A[59])
    #print(A[60])
    #print(A[61])
    #print(A[62])
    #print(A[63])
    #print(A[64

=======
Suggestion 8

def main():
    N, W = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    # おもりの重さの和がiになるようなおもりの組み合わせの数
    dp = [0] * (W + 1)
    dp[0] = 1
    for a in A:
        for i in range(W, a - 1, -1):
            dp[i] += dp[i - a]
    print(dp[W])

=======
Suggestion 9

def get_good_integers(W, A):
    A = sorted(A)
    #print(A)
    good_integers = set()
    for i in range(2**len(A)):
        #print("i=", i)
        total = 0
        for j in range(len(A)):
            #print("j=", j)
            if i & (1<<j):
                #print("i=", i, "j=", j)
                total += A[j]
                #print("total=", total)
        if total <= W:
            good_integers.add(total)
    return len(good_integers)
