Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n, k = map(int, input().split())
    c = list(map(int, input().split()))
    ans = 0
    d = {}
    for i in range(k):
        if c[i] not in d:
            d[c[i]] = 1
        else:
            d[c[i]] += 1
    ans = len(d)
    for i in range(k, n):
        if d[c[i-k]] == 1:
            del d[c[i-k]]
        else:
            d[c[i-k]] -= 1
        if c[i] not in d:
            d[c[i]] = 1
        else:
            d[c[i]] += 1
        ans = max(ans, len(d))
    print(ans)

=======
Suggestion 2

def main():
    n, k = map(int, input().split())
    c = list(map(int, input().split()))

    count = {}
    for i in range(k):
        if c[i] in count:
            count[c[i]] += 1
        else:
            count[c[i]] = 1

    ans = len(count)

    for i in range(k, n):
        if c[i] in count:
            count[c[i]] += 1
        else:
            count[c[i]] = 1

        if count[c[i-k]] == 1:
            count.pop(c[i-k])
        else:
            count[c[i-k]] -= 1

        ans = max(ans, len(count))

    print(ans)

=======
Suggestion 3

def main():
    N, K = map(int, input().split())
    c = list(map(int, input().split()))
    color = []
    for i in range(N-K+1):
        color.append(len(set(c[i:i+K])))
    print(max(color))

=======
Suggestion 4

def main():
    N, K = map(int, input().split())
    c = list(map(int, input().split()))
    candy = dict()
    for i in range(K):
        if c[i] in candy:
            candy[c[i]] += 1
        else:
            candy[c[i]] = 1
    max_candy = len(candy)
    for i in range(K, N):
        if c[i] in candy:
            candy[c[i]] += 1
        else:
            candy[c[i]] = 1
        if candy[c[i-K]] == 1:
            candy.pop(c[i-K])
        else:
            candy[c[i-K]] -= 1
        if len(candy) > max_candy:
            max_candy = len(candy)
    print(max_candy)

=======
Suggestion 5

def main():
    N, K = map(int, input().split())
    c = list(map(int, input().split()))
    ans = 0
    tmp = 0
    dic = {}
    for i in range(N):
        if i < K:
            if c[i] not in dic:
                dic[c[i]] = 1
                tmp += 1
            else:
                dic[c[i]] += 1
        else:
            if c[i] not in dic:
                dic[c[i]] = 1
                tmp += 1
            else:
                dic[c[i]] += 1
            if c[i-K] in dic:
                dic[c[i-K]] -= 1
                if dic[c[i-K]] == 0:
                    tmp -= 1
            if tmp > ans:
                ans = tmp
    print(ans)

=======
Suggestion 6

def main():
    n,k = map(int,input().split())
    c = list(map(int,input().split()))

    ans = 0
    cnt = {}
    for i in range(n):
        if i >= k:
            cnt[c[i-k]] -= 1
            if cnt[c[i-k]] == 0:
                del cnt[c[i-k]]
        if c[i] not in cnt:
            cnt[c[i]] = 0
        cnt[c[i]] += 1
        ans = max(ans,len(cnt))
    print(ans)

=======
Suggestion 7

def main():
    N, K = map(int, input().split())
    c = list(map(int, input().split()))
    #print(N, K)
    #print(c)
    #print(len(c))
    #print(c[0])
    #print(c[1])
    #print(c[2])
    #print(c[3])
    #print(c[4])
    #print(c[5])
    #print(c[6])
    #print(c[7])
    #print(c[8])
    #print(c[9])
    #print(c[10])
    #print(c[11])
    #print(c[12])
    #print(c[13])
    #print(c[14])
    #print(c[15])
    #print(c[16])
    #print(c[17])
    #print(c[18])
    #print(c[19])
    #print(c[20])
    #print(c[21])
    #print(c[22])
    #print(c[23])
    #print(c[24])
    #print(c[25])
    #print(c[26])
    #print(c[27])
    #print(c[28])
    #print(c[29])
    #print(c[30])
    #print(c[31])
    #print(c[32])
    #print(c[33])
    #print(c[34])
    #print(c[35])
    #print(c[36])
    #print(c[37])
    #print(c[38])
    #print(c[39])
    #print(c[40])
    #print(c[41])
    #print(c[42])
    #print(c[43])
    #print(c[44])
    #print(c[45])
    #print(c[46])
    #print(c[47])
    #print(c[48])
    #print(c[49])
    #print(c[50])
    #print(c[51])
    #print(c[52])
    #print(c[53])
    #print(c[54])
    #print(c[55])
    #print(c[56])
    #print(c[57])
    #print(c[58])
    #print(c[59])
    #print(c[60])
    #print(c[61])
    #print(c[62])
    #print(c[63])
    #print(c[64])
    #

=======
Suggestion 8

def main():
    N, K = map(int, input().split())
    C = list(map(int, input().split()))
    ans = 0
    color = [0] * 1000010
    for i in range(N):
        color[C[i]] += 1
        if i >= K:
            color[C[i-K]] -= 1
        ans = max(ans, len([i for i in color if i > 0]))
    print(ans)

=======
Suggestion 9

def main():
    N, K = map(int, input().split())
    c = list(map(int, input().split()))
    #print(N, K)
    #print(c)
    #print(len(c))
    #print(type(c))
    #print(type(c[0]))
    #print(c[0])
    #print(c[1])
    #print(c[2])
    #print(c[3])
    #print(c[4])
    #print(c[5])
    #print(c[6])
    #print(c[7])
    #print(c[8])
    #print(c[9])
    #print(c[10])
    #print(c[11])
    #print(c[12])
    #print(c[13])
    #print(c[14])
    #print(c[15])
    #print(c[16])
    #print(c[17])
    #print(c[18])
    #print(c[19])
    #print(c[20])
    #print(c[21])
    #print(c[22])
    #print(c[23])
    #print(c[24])
    #print(c[25])
    #print(c[26])
    #print(c[27])
    #print(c[28])
    #print(c[29])
    #print(c[30])
    #print(c[31])
    #print(c[32])
    #print(c[33])
    #print(c[34])
    #print(c[35])
    #print(c[36])
    #print(c[37])
    #print(c[38])
    #print(c[39])
    #print(c[40])
    #print(c[41])
    #print(c[42])
    #print(c[43])
    #print(c[44])
    #print(c[45])
    #print(c[46])
    #print(c[47])
    #print(c[48])
    #print(c[49])
    #print(c[50])
    #print(c[51])
    #print(c[52])
    #print(c[53])
    #print(c[54])
    #print(c[55])
    #print(c[56])
    #print(c[57])
    #print(c[58])
    #print(c[59])
    #print(c[60])
    #print(c[61])
    #print(c[62])
    #

=======
Suggestion 10

def main():
    N, K = map(int, input().split())
    c = list(map(int, input().split()))
    # print(N, K, c)
    # print(type(N), type(K), type(c))
    # print(len(c))
    # print(c[0])
    # print(c[1])
    # print(c[2])
    # print(c[3])
    # print(c[4])
    # print(c[5])
    # print(c[6])
    # print(c[7])
    # print(c[8])
    # print(c[9])
    # print(c[10])
    # print(c[11])
    # print(c[12])
    # print(c[13])
    # print(c[14])
    # print(c[15])
    # print(c[16])
    # print(c[17])
    # print(c[18])
    # print(c[19])
    # print(c[20])
    # print(c[21])
    # print(c[22])
    # print(c[23])
    # print(c[24])
    # print(c[25])
    # print(c[26])
    # print(c[27])
    # print(c[28])
    # print(c[29])
    # print(c[30])
    # print(c[31])
    # print(c[32])
    # print(c[33])
    # print(c[34])
    # print(c[35])
    # print(c[36])
    # print(c[37])
    # print(c[38])
    # print(c[39])
    # print(c[40])
    # print(c[41])
    # print(c[42])
    # print(c[43])
    # print(c[44])
    # print(c[45])
    # print(c[46])
    # print(c[47])
    # print(c[48])
    # print(c[49])
    # print(c[50])
    # print(c[51])
    # print(c[52])
    # print(c[53])
    # print(c[54])
    # print(c[55])
    # print(c[56])
    # print(c[57])
    # print(c[58])
    # print(c[59])
    # print(c[60])
    # print(c[61])
    # print(c[62])
    # print(c[63])
