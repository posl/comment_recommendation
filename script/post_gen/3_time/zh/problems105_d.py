Synthesizing 10/10 solutions

=======
Suggestion 1

def num_of_divisible_subarray(nums, m):
    n = len(nums)
    num_of_divisible_subarray = 0
    for i in range(n):
        sum = 0
        for j in range(i, n):
            sum += nums[j]
            if sum % m == 0:
                num_of_divisible_subarray += 1
    return num_of_divisible_subarray

=======
Suggestion 2

def main():
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    for i in range(n):
        if a[i]%m==0:
            a[i]=0
        else:
            a[i]=a[i]%m
    for i in range(1,n):
        a[i] += a[i-1]
    mod = {}
    for i in range(n):
        if a[i] in mod:
            mod[a[i]] += 1
        else:
            mod[a[i]] = 1
    ans = 0
    for key in mod:
        ans += mod[key]*(mod[key]-1)//2
    ans += mod[0]
    print(ans)

=======
Suggestion 3

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    #print(A)
    #print(N, M)
    #print(len(A))
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
    #print(A[64])
    #

=======
Suggestion 4

def main():
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    s = [0]*(n+1)
    for i in range(n):
        s[i+1] = s[i]+a[i]
    d = {}
    for i in range(n+1):
        s[i] %= m
        if s[i] in d:
            d[s[i]] += 1
        else:
            d[s[i]] = 1
    ans = 0
    for x in d:
        ans += d[x]*(d[x]-1)//2
    print(ans)

=======
Suggestion 5

def getSum(A, l, r):
    sum = 0
    for i in range(l, r+1):
        sum += A[i]
    return sum

=======
Suggestion 6

def get_input():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    return N, M, A

=======
Suggestion 7

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    for i in range(n):
        a[i] %= m
    s = [0]
    for i in range(n):
        s.append((s[-1] + a[i]) % m)
    from collections import Counter
    c = Counter(s)
    ans = 0
    for x in c:
        ans += c[x] * (c[x] - 1) // 2
    print(ans)

=======
Suggestion 8

def problem105_d():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    s = [0]
    for i in range(n):
        s.append(s[i] + a[i])
    s = [x % m for x in s]
    s.sort()
    ans = 0
    prev = 0
    cnt = 0
    for x in s:
        if x == prev:
            cnt += 1
        else:
            ans += cnt * (cnt - 1) // 2
            prev = x
            cnt = 1
    ans += cnt * (cnt - 1) // 2
    print(ans)

=======
Suggestion 9

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    for i in range(N):
        A[i] = A[i] % M
    S = [0] * (N + 1)
    for i in range(N):
        S[i + 1] = S[i] + A[i]
        S[i + 1] %= M
    S.sort()
    ans = 0
    cnt = 1
    for i in range(N):
        if S[i] == S[i + 1]:
            cnt += 1
        else:
            ans += cnt * (cnt - 1) // 2
            cnt = 1
    ans += cnt * (cnt - 1) // 2
    print(ans)

main()

=======
Suggestion 10

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    ans = 0
    sum_a = [0] * (n + 1)
    for i in range(n):
        sum_a[i + 1] = sum_a[i] + a[i]
        sum_a[i + 1] %= m
    from collections import Counter
    c = Counter(sum_a)
    for v in c.values():
        ans += v * (v - 1) // 2
    print(ans)
