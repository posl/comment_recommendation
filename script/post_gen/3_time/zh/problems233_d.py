Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    # print(N, K)
    # print(A)
    # print(len(A))
    count = 0
    for i in range(N):
        for j in range(i+1,N+1):
            # print(i,j)
            # print(A[i:j])
            if sum(A[i:j]) == K:
                count += 1
    print(count)

=======
Suggestion 2

def main():
    pass

=======
Suggestion 3

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    count = 0
    for i in range(N):
        temp = 0
        for j in range(i, N):
            temp += A[j]
            if temp == K:
                count += 1
    print(count)

=======
Suggestion 4

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    # print(n, k)
    # print(a)
    # print(len(a))
    # print(a[0])
    # print(a[1])
    # print(a[2])
    # print(a[3])
    # print(a[4])
    # print(a[5])
    # print(a[6])
    # print(a[7])
    # print(a[8])
    # print(a[9])
    # print(a[10])
    # print(a[11])
    # print(a[12])
    # print(a[13])
    # print(a[14])
    # print(a[15])
    # print(a[16])
    # print(a[17])
    # print(a[18])
    # print(a[19])
    # print(a[20])
    # print(a[21])
    # print(a[22])
    # print(a[23])
    # print(a[24])
    # print(a[25])
    # print(a[26])
    # print(a[27])
    # print(a[28])
    # print(a[29])
    # print(a[30])
    # print(a[31])
    # print(a[32])
    # print(a[33])
    # print(a[34])
    # print(a[35])
    # print(a[36])
    # print(a[37])
    # print(a[38])
    # print(a[39])
    # print(a[40])
    # print(a[41])
    # print(a[42])
    # print(a[43])
    # print(a[44])
    # print(a[45])
    # print(a[46])
    # print(a[47])
    # print(a[48])
    # print(a[49])
    # print(a[50])
    # print(a[51])
    # print(a[52])
    # print(a[53])
    # print(a[54])
    # print(a[55])
    # print(a[56])
    # print(a[57])
    # print(a[58])
    # print(a[59])
    # print(a[60])
    # print(a[61])
    # print(a[62])
    # print(a[63])
    # print(a[64])
    #

=======
Suggestion 5

def solve():
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    s=[0]*(n+1)
    for i in range(n):
        s[i+1]=s[i]+a[i]
    from collections import defaultdict
    d=defaultdict(int)
    for i in range(n+1):
        d[s[i]]+=1
    ans=0
    for i in range(n+1):
        ans+=d[s[i]-k]
        d[s[i]]-=1
    print(ans)
solve()

=======
Suggestion 6

def subseq_sum(A, K):
    N = len(A)
    s = [0]
    for i in range(N):
        s.append(s[-1]+A[i])
    #print(s)
    from collections import defaultdict
    d = defaultdict(int)
    for i in range(N+1):
        d[s[i]] += 1
    #print(d)
    ans = 0
    for i in range(N+1):
        ans += d[s[i]-K]
    return ans

=======
Suggestion 7

def solve():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    # print(n, k)
    # print(a)
    # for i in range(n):
    #     print(a[i])
    # print(a[0])
    # print(a[1])
    # print(a[2])
    # print(a[3])
    # print(a[4])
    # print(a[5])
    # print(a[6])
    # print(a[7])
    # print(a[8])
    # print(a[9])
    # print(a[10])
    # print(a[11])
    # print(a[12])
    # print(a[13])
    # print(a[14])
    # print(a[15])
    # print(a[16])
    # print(a[17])
    # print(a[18])
    # print(a[19])
    # print(a[20])
    # print(a[21])
    # print(a[22])
    # print(a[23])
    # print(a[24])
    # print(a[25])
    # print(a[26])
    # print(a[27])
    # print(a[28])
    # print(a[29])
    # print(a[30])
    # print(a[31])
    # print(a[32])
    # print(a[33])
    # print(a[34])
    # print(a[35])
    # print(a[36])
    # print(a[37])
    # print(a[38])
    # print(a[39])
    # print(a[40])
    # print(a[41])
    # print(a[42])
    # print(a[43])
    # print(a[44])
    # print(a[45])
    # print(a[46])
    # print(a[47])
    # print(a[48])
    # print(a[49])
    # print(a[50])
    # print(a[51])
    # print(a[52])
    # print(a[53])
    # print(a[54])
    # print(a[55])
    # print(a[56])
    # print(a[57])
    # print(a[58])
    # print(a[59])
    # print(a[60])
    # print(a[61])
    # print(a[62])
    # print(a[63])

=======
Suggestion 8

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    #print(N, K, A)
    sum = 0
    for i in range(N):
        sum += A[i]
    #print(sum)
    if sum < K:
        print(0)
        return
    else:
        pass
    #print(A)
    #print(len(A))
    for i in range(N):
        if A[i] == K:
            print(1)
            return
        else:
            pass
    #print("OK")
    for i in range(N):
        if A[i] > K:
            A[i] = 0
        else:
            pass
    #print(A)
    for i in range(N):
        if A[i] == 0:
            A[i] = 1
        else:
            pass
    #print(A)
    for i in range(N):
        if i == 0:
            pass
        else:
            A[i] += A[i-1]
    #print(A)
    for i in range(N):
        if A[i] == K:
            print(1)
            return
        else:
            pass
    #print("OK")
    for i in range(N):
        if A[i] < K:
            A[i] = 0
        else:
            pass
    #print(A)
    for i in range(N):
        if A[i] == 0:
            A[i] = 1
        else:
            pass
    #print(A)
    for i in range(N):
        if i == 0:
            pass
        else:
            A[i] += A[i-1]
    #print(A)
    for i in range(N):
        if A[i] == K:
            print(1)
            return
        else:
            pass
    #print("OK")
    for i in range(N):
        if A[i] > K:
            A[i] = 0
        else:
            pass
    #print(A)
    for i in range(N):
        if A[i] == 0:
            A[i] = 1
        else:
            pass
    #print(A)
    for i in range(N):
        if i == 0:
            pass
        else:
            A[i] += A[i-1

=======
Suggestion 9

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a.insert(0, 0)
    s = [0]
    for i in range(1, n+1):
        s.append(s[i-1]+a[i])
    ans = 0
    sum = {}
    for i in range(1, n+1):
        if s[i]-k in sum:
            ans += sum[s[i]-k]
        if s[i] in sum:
            sum[s[i]] += 1
        else:
            sum[s[i]] = 1
    print(ans)
