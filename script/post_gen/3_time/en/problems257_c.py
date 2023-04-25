Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    S = input()
    W = list(map(int, input().split()))
    children = []
    adults = []
    for i in range(N):
        if S[i] == '0':
            children.append(W[i])
        else:
            adults.append(W[i])
    children.sort()
    adults.sort()
    if len(children) == 0:
        print(0)
        return
    if len(adults) == 0:
        print(len(children))
        return
    ans = 0
    for i in range(len(adults)):
        ans += (adults[i] >= children[i])
    print(ans)

=======
Suggestion 2

def main():
    N = int(input())
    S = input()
    W = list(map(int, input().split()))
    child = []
    adult = []
    for i in range(N):
        if S[i] == "0":
            child.append(W[i])
        else:
            adult.append(W[i])
    child.sort()
    adult.sort()
    child_sum = sum(child)
    adult_sum = sum(adult)
    child_acc = [0]
    adult_acc = [0]
    for i in range(len(child)):
        child_acc.append(child_acc[-1] + child[i])
    for i in range(len(adult)):
        adult_acc.append(adult_acc[-1] + adult[i])
    max_count = 0
    for i in range(len(child_acc)):
        adult_count = 0
        for j in range(len(adult_acc)):
            if child_acc[i] + adult_acc[j] <= adult_sum:
                adult_count = j
            else:
                break
        max_count = max(max_count, i + adult_count)
    print(max_count)

=======
Suggestion 3

def main():
    n=int(input())
    s=input()
    w=list(map(int,input().split()))
    w1=[w[i] for i in range(n) if s[i]=='1']
    w0=[w[i] for i in range(n) if s[i]=='0']
    w1.sort()
    w0.sort()
    w0.reverse()
    ans=0
    for i in range(1,len(w1)+1):
        j=len(w0)-i
        if j>=0:
            ans=max(ans,sum(w1[:i])+sum(w0[:j]))
        else:
            ans=max(ans,sum(w1[:i]))
    print(ans)

=======
Suggestion 4

def main():
    N = int(input())
    S = input()
    W = list(map(int, input().split()))
    #print(N)
    #print(S)
    #print(W)
    #print(len(S))
    #print(len(W))
    #print(W[0])
    #print(W[1])
    #print(W[2])
    #print(W[3])
    #print(W[4])
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

=======
Suggestion 5

def main():
    N = int(input())
    S = input()
    W = list(map(int,input().split()))

    ans = 0
    for i in range(1,N):
        if S[i-1] == S[i]:
            ans += 1
    print(ans)

=======
Suggestion 6

def main():
    N = int(input())
    S = input()
    W = [int(w) for w in input().split()]
    ans = 0
    for i in range(1, N):
        if S[i - 1] == '0' and S[i] == '1':
            ans += 1
    if S[-1] == '0':
        ans += 1
    print(ans)

=======
Suggestion 7

def main():
    n = int(input())
    s = input()
    w = list(map(int, input().split()))
    ans = 0
    for i in range(1,n):
        if s[i-1] == "0" and s[i] == "1":
            ans += 1
    if ans == 0:
        print(0)
        exit()
    ans += 2
    ans -= 1 if s[0] == "0" else 0
    ans -= 1 if s[-1] == "0" else 0
    for i in range(n):
        if s[i] == "0":
            if i == 0:
                ans += 1 if w[i] < w[i+1] else 0
            elif i == n-1:
                ans += 1 if w[i-1] < w[i] else 0
            else:
                ans += 1 if w[i-1] < w[i] and w[i] > w[i+1] else 0
    print(ans)

=======
Suggestion 8

def main():
    N = int(input())
    S = input()
    W = list(map(int, input().split()))
    w_c = [0]
    w_a = [0]
    for i in range(N):
        w_c.append(w_c[i])
        w_a.append(w_a[i])
        if S[i] == '0':
            w_c[i+1] += W[i]
        else:
            w_a[i+1] += W[i]
    ans = 0
    for i in range(N+1):
        ans = max(ans, w_c[i]+w_a[N]-w_a[i])
    print(ans)

=======
Suggestion 9

def main():
    N = int(input())
    S = input()
    W = [int(w) for w in input().split()]
    #print(N)
    #print(S)
    #print(W)
    #print(sum(W))
    #print(sum(W[0:3]))
    #print(sum(W[3:5]))
    x = 0
    y = 0
    ans = 0
    for i in range(N):
        if S[i] == '0':
            x += W[i]
        else:
            y += W[i]
    ans = abs(x-y)
    for i in range(N):
        if S[i] == '0':
            x += W[i]
        else:
            y += W[i]
        ans = max(ans,abs(x-y))
    print(ans)

=======
Suggestion 10

def main():
    # input
    N = int(input())
    S = input()
