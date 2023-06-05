Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n,k = map(int,input().split())
    s = input()
    start = s[0]
    if start == "R":
        s = s[::-1]
    s = s.repl

=======
Suggestion 2

def happy_people(S):
    n = len(S)
    happy = 0
    for i in range(n-1):
        if S[i] == S[i+1]:
            happy += 1
    return happy

=======
Suggestion 3

def main():
    N,K = map(int,input().split())
    S = input()
    L = []
    for i in range(N):
        if S[i] == "L":
            L.append(i)
    R = []
    for i in range(N):
        if S[i] == "R":
            R.append(i)
    A = []
    for i in range(len(L)-1):
        A.append(L[i+1]-L[i])
    B = []
    for i in range(len(R)-1):
        B.append(R[i+1]-R[i])
    if len(A) == 0 and len(B) == 0:
        print(N)
        return
    if len(A) == 0:
        A.append(100000)
    if len(B) == 0:
        B.append(100000)
    A.sort()
    B.sort()
    if len(A) == 1:
        print(min(N,A[0]+2*K))
        return
    if len(B) == 1:
        print(min(N,B[0]+2*K))
        return
    ans = 0
    for i in range(len(A)):
        if i == 0:
            ans = max(ans,A[i]+K)
        else:
            ans = max(ans,A[i]//2)
    for i in range(len(B)):
        if i == 0:
            ans = max(ans,B[i]+K)
        else:
            ans = max(ans,B[i]//2)
    print(min(N,ans+K))

=======
Suggestion 4

def main():
    N,K = map(int, input().split())
    S = input()
    count = 0
    for i in range(N-1):
        if S[i] == S[i+1]:
            count += 1
    ans = min(N-1, count+2*K)
    print(ans)

=======
Suggestion 5

def get_happiness_num(n, k, s):
    # 从左到右遍历，找到第一个不快乐的人，然后从右向左遍历，找到第一个不快乐的人，然后将两者之间的人全部旋转
    # 再重复上面的操作，直到k次循环结束
    # 如果到最后还有不快乐的人，则将最后一个人旋转
    # 旋转后，不快乐的人数减少，快乐的人数增加
    # 如果旋转后，不快乐的人数不减少，则不再旋转
    # 旋转的过程中，记录下快乐的人数
    # 如果快乐的人数不再增加，则不再旋转

    # 初始化
    # 从左向右遍历，找到第一个不快乐的人
    # 从右向左遍历，找到第一个不快乐的人
    # 旋转两者之间的人
    # 旋转后，不快乐的人数减少，快乐的人数增加
    # 如果旋转后，不快乐的人数不减少，则不再旋转
    # 旋转的过程中，记录下快乐的人数
    # 如果快乐的人数不再增加，则不再旋转
    # 重复上述操作，直到k次循环结束
    # 如果到最后还有不快乐的人，则将最后一个人旋转
    # 旋转后，不快乐的人数减少，快乐的人数增加
    # 如果旋转后，不快乐的人数不减少，则不再旋转
    # 旋转的过程中，记录下快乐的人数
    # 如果

=======
Suggestion 6

def main():
    n,k = map(int, input().split())
    s = input()
    s = s.replace('RL','LR')
    s = s.replace('LR','RL')
    s = s.replace('LL','L')
    s = s.replace('RR','R')
    cnt = 0
    for i in range(1, len(s)):
        if s[i-1] == s[i]:
            cnt += 1
    print(min(n-1, cnt+2*k))

=======
Suggestion 7

def main():
    n,k = map(int,input().split())
    s = input()
    #print(n,k,s)
    count = 0
    for i in range(n-1):
        if s[i] == s[i+1]:
            count += 1
    count = min(count+2*k,n-1)
    print(count)

=======
Suggestion 8

def main():
    N, K = map(int, input().split())
    S = input()
    S = list(S)
    S.insert(0, '0')
    S.append('0')
    #print(S)
    happy = 0
    for i in range(1, N+1):
        if S[i] == 'L' and S[i-1] == 'L':
            happy += 1
        elif S[i] == 'R' and S[i+1] == 'R':
            happy += 1
    #print(happy)
    if K > happy:
        K = happy
    #print(K)
    for i in range(1, N+1):
        if S[i] == 'L' and S[i-1] == 'R':
            S[i] = 'R'
            happy += 1
        elif S[i] == 'R' and S[i+1] == 'L':
            S[i] = 'L'
            happy += 1
        if happy == K:
            break
    #print(S)
    happy = 0
    for i in range(1, N+1):
        if S[i] == 'L' and S[i-1] == 'L':
            happy += 1
        elif S[i] == 'R' and S[i+1] == 'R':
            happy += 1
    print(happy)

=======
Suggestion 9

def main():
    N,K = map(int,input().split())
    S = input()
    cnt = 0
    for i in range(N-1):
        if S[i] == S[i+1]:
            cnt += 1
    print(min(cnt+2*K,N-1))

=======
Suggestion 10

def main():
    N,K = map(int,input().split())
    S = input()
    S = list(S)
    S = list(map(lambda x:1 if x == 'L' else 0,S))
    #print(S)
    #print(N,K)
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
