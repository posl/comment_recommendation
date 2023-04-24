Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, K = map(int, input().split())
    S = input()
    ans = 0
    for i in range(N):
        if S[i] == '0':
            cnt = 0
            for j in range(i, N):
                if S[j] == '0':
                    cnt += 1
                else:
                    break
            ans = max(ans, cnt)
        else:
            cnt = 0
            for j in range(i, N):
                if S[j] == '1':
                    cnt += 1
                else:
                    break
            ans = max(ans, cnt)
    ans = min(N, ans + K * 2)
    print(ans)

=======
Suggestion 2

def main():
    N, K = map(int, input().split())
    S = input()
    ans = 0
    for i in range(N):
        if S[i] == "0":
            j = i
            while j < N and S[j] == "0":
                j += 1
            ans = max(ans, j - i)
    print(min(ans + 2 * K, N))

main()

=======
Suggestion 3

def solve():
    N, K = map(int, input().split())
    S = input()
    ans = 0
    for i in range(N):
        if S[i] == "0":
            j = i
            while j < N and S[j] == "0":
                j += 1
            ans = max(ans, j - i)
    for i in range(N):
        if S[i] == "1":
            j = i
            while j < N and S[j] == "1":
                j += 1
            ans = max(ans, j - i)
    if ans == N:
        ans += K * 2
    else:
        ans += K
    print(min(ans, N))

solve()

=======
Suggestion 4

def main():
    N, K = map(int, input().split())
    S = input()
    ans = 0
    for i in range(N):
        if S[i] == "0":
            ans += 1
            for j in range(i+1, N):
                if S[j] == "1":
                    ans += 1
                else:
                    break
            break
    for i in range(N-1, -1, -1):
        if S[i] == "0":
            ans += 1
            for j in range(i-1, -1, -1):
                if S[j] == "1":
                    ans += 1
                else:
                    break
            break
    cnt = 0
    for i in range(N):
        if S[i] == "1":
            cnt += 1
        else:
            cnt = 0
        ans = max(ans, cnt)
    print(min(ans+2*K, N))

=======
Suggestion 5

def main():
    n, k = map(int, input().split())
    s = input()
    c = 0
    l = 0
    r = 0
    ans = 0
    while r < n:
        if s[r] == '0':
            c += 1
        while c > k:
            if s[l] == '0':
                c -= 1
            l += 1
        ans = max(ans, r-l+1)
        r += 1
    print(ans)

=======
Suggestion 6

def main():
    N, K = map(int, input().split())
    S = input()
    if N == 1:
        print(1)
        return
    if N == K:
        print(N)
        return
    if N == K + 1:
        if S[0] == '0' or S[-1] == '0':
            print(N)
        else:
            print(N - 1)
        return
    if S[0] == '0':
        S = '0' + S
    if S[-1] == '0':
        S = S + '0'
    S = S + S
    N = len(S)
    #print(S)
    #print(N)
    start = []
    end = []
    for i in range(N):
        if S[i] == '0':
            start.append(i)
        else:
            end.append(i)
    #print(start)
    #print(end)
    ans = 0
    for i in range(len(start)):
        if i == 0:
            ans = max(ans, end[i])
        else:
            ans = max(ans, end[i] - start[i - 1])
    print(ans)

=======
Suggestion 7

def main():
    N, K = map(int, input().split())
    S = input()
    ans = 0
    for i in range(N):
        if S[i] == '1':
            continue
        if S[i] == '0':
            if i == 0:
                ans = 1
                j = i + 1
                while j < N:
                    if S[j] == '0':
                        ans += 1
                        j += 1
                    else:
                        break
                break
            if S[i - 1] == '0':
                ans = 1
                j = i + 1
                while j < N:
                    if S[j] == '0':
                        ans += 1
                        j += 1
                    else:
                        break
                break
    print(ans)

=======
Suggestion 8

def main():
    N, K = map(int, input().split())
    S = input()
    L = []
    l = 0
    for i in range(N):
        if i == N-1:
            L.append(i-l+1)
        elif S[i] != S[i+1]:
            L.append(i-l+1)
            l = i+1
    if len(L) == 1:
        print(N)
        return
    if S[0] == "1":
        L = [0] + L
    if S[-1] == "1":
        L = L + [0]
    if len(L) <= 2*K + 1:
        print(N)
        return
    ans = 0
    for i in range(0, len(L)-2*K, 2):
        ans = max(ans, sum(L[i:i+2*K+1]))
    print(ans)

=======
Suggestion 9

def main():
    N, K = map(int, input().split())
    S = input()
    S = S.replace("0", "1").replace("1", "0")
    #print(S)
    #print(S[0])
    #print(S[1])
    #print(S[2])
    #print(S[3])
    #print(S[4])
    #print(S[5])
    #print(S[6])
    #print(S[7])
    #print(S[8])
    #print(S[9])
    #print(S[10])
    #print(S[11])
    #print(S[12])
    #print(S[13])
    #print(S[14])
    #print(S[15])
    #print(S[16])
    #print(S[17])
    #print(S[18])
    #print(S[19])
    #print(S[20])
    #print(S[21])
    #print(S[22])
    #print(S[23])
    #print(S[24])
    #print(S[25])
    #print(S[26])
    #print(S[27])
    #print(S[28])
    #print(S[29])
    #print(S[30])
    #print(S[31])
    #print(S[32])
    #print(S[33])
    #print(S[34])
    #print(S[35])
    #print(S[36])
    #print(S[37])
    #print(S[38])
    #print(S[39])
    #print(S[40])
    #print(S[41])
    #print(S[42])
    #print(S[43])
    #print(S[44])
    #print(S[45])
    #print(S[46])
    #print(S[47])
    #print(S[48])
    #print(S[49])
    #print(S[50])
    #print(S[51])
    #print(S[52])
    #print(S[53])
    #print(S[54])
    #print(S[55])
    #print(S[56])
    #print(S[57])
    #print(S[58])
    #print(S[59])
    #print(S[60])
    #print(S[61])
    #print(S[62])
    #print(S[63])
    #print(S[64])
    #print

=======
Suggestion 10

def main():
    N, K = map(int, input().split())
    S = input()
    
    # 0: feet, 1: hands
