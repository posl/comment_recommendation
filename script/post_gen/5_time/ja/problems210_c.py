Synthesizing 9/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n, k = map(int, input().split())
    c = list(map(int, input().split()))
    ans = 0
    for i in range(n-k+1):
        ans = max(ans, len(set(c[i:i+k])))
    print(ans)

=======
Suggestion 2

def main():
    n,k = map(int,input().split())
    c = list(map(int,input().split()))
    d = {}
    for i in range(k):
        if c[i] not in d:
            d[c[i]] = 1
        else:
            d[c[i]] += 1
    ans = len(d)
    for i in range(n-k):
        if d[c[i]] == 1:
            del d[c[i]]
        else:
            d[c[i]] -= 1
        if c[i+k] not in d:
            d[c[i+k]] = 1
        else:
            d[c[i+k]] += 1
        ans = max(ans,len(d))
    print(ans)
main()

=======
Suggestion 3

def main():
    n,k = map(int, input().split())
    c = list(map(int, input().split()))
    #print(n,k,c)
    #print(len(c))
    #print(len(set(c)))
    #print(len(c)-len(set(c)))
    #print(n-k)
    #print(len(c)-len(set(c)) - (n-k))
    if k == 1:
        print(1)
        exit()
    if len(c)-len(set(c)) - (n-k) < 0:
        print(len(set(c)))
        exit()
    print(len(set(c)) - (len(c)-len(set(c)) - (n-k)))

=======
Suggestion 4

def main():
    N, K = map(int, input().split())
    c = list(map(int, input().split()))
    #print(N, K, c)
    #print(len(c))
    #print(c[0:K])
    #print(c[1:K+1])
    #print(c[2:K+2])
    #print(c[3:K+3])
    #print(c[4:K+4])
    #print(c[5:K+5])
    #print(c[6:K+6])
    #print(c[7:K+7])
    #print(c[8:K+8])
    #print(c[9:K+9])
    #print(c[10:K+10])
    #print(c[11:K+11])
    #print(c[12:K+12])
    #print(c[13:K+13])
    #print(c[14:K+14])
    #print(c[15:K+15])
    #print(c[16:K+16])
    #print(c[17:K+17])
    #print(c[18:K+18])
    #print(c[19:K+19])
    #print(c[20:K+20])
    #print(c[21:K+21])
    #print(c[22:K+22])
    #print(c[23:K+23])
    #print(c[24:K+24])
    #print(c[25:K+25])
    #print(c[26:K+26])
    #print(c[27:K+27])
    #print(c[28:K+28])
    #print(c[29:K+29])
    #print(c[30:K+30])
    #print(c[31:K+31])
    #print(c[32:K+32])
    #print(c[33:K+33])
    #print(c[34:K+34])
    #print(c[35:K+35])
    #print(c[36:K+36])
    #print(c[37:K+37])
    #print(c[38:K+38])
    #print(c[39:K+39])
    #print(c[40:K+40])
    #print(c[41:K+41])

=======
Suggestion 5

def main():
    N,K = map(int,input().split())
    c = list(map(int,input().split()))
    ans = 0
    dic = {}
    for i in range(K):
        if c[i] in dic:
            dic[c[i]] += 1
        else:
            dic[c[i]] = 1
    ans = len(dic)
    for i in range(K,N):
        if c[i] in dic:
            dic[c[i]] += 1
        else:
            dic[c[i]] = 1
        dic[c[i-K]] -= 1
        if dic[c[i-K]] == 0:
            del dic[c[i-K]]
        ans = max(ans,len(dic))
    print(ans)

=======
Suggestion 6

def main():
    N, K = map(int, input().split())
    c = list(map(int, input().split()))
    ans = 0
    for i in range(N-K+1):
        ans = max(ans, len(set(c[i:i+K])))
    print(ans)

=======
Suggestion 7

def main():
    n,k = map(int, input().split())
    c = list(map(int, input().split()))
    #print(n,k,c)
    count = 0
    for i in range(n-k+1):
        count = max(len(set(c[i:i+k])), count)
    print(count)
main()

=======
Suggestion 8

def main():
    n,k = map(int,input().split())
    c = list(map(int,input().split()))
    d = {}
    for i in range(k):
        if c[i] in d:
            d[c[i]] += 1
        else:
            d[c[i]] = 1
    ans = len(d)
    for i in range(k,n):
        if c[i] in d:
            d[c[i]] += 1
        else:
            d[c[i]] = 1
        if d[c[i-k]] == 1:
            del d[c[i-k]]
        else:
            d[c[i-k]] -= 1
        ans = max(ans,len(d))
    print(ans)
