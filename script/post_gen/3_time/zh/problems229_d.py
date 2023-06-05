Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    s = input()
    k = int(input())
    max = 0
    count = 0
    for i in range(len(s)):
        if s[i] == '.':
            count += 1
        else:
            if max < count:
                max = count
            count = 0
    if max < count:
        max = count
    if max > k:
        print(max-k)
    else:
        print(0)

=======
Suggestion 2

def main():
    s = input()
    k = int(input())
    n = len(s)
    if k >= n:
        print(n)
        return
    max_x = 0
    cur = 0
    for i in range(n):
        if s[i] == 'X':
            cur += 1
        else:
            if cur > max_x:
                max_x = cur
            cur = 0
    if cur > max_x:
        max_x = cur
    if k == 0:
        print(max_x)
        return
    cur = 0
    for i in range(n):
        if s[i] == '.':
            cur += 1
        else:
            if cur > max_x:
                max_x = cur
            cur = 0
    if cur > max_x:
        max_x = cur
    if k == 1:
        print(max_x + 1)
        return
    cur = 0
    for i in range(n):
        if s[i] == '.':
            cur += 1
        else:
            if cur > max_x:
                max_x = cur
            cur = 0
    if cur > max_x:
        max_x = cur
    print(max_x + k)

=======
Suggestion 3

def main():
    s = input()
    k = int(input())
    s = list(s)
    s.append('X')
    s.insert(0, 'X')
    s.append('X')
    s.insert(0, 'X')
    ans = 0
    for i in range(1, len(s)):
        if s[i] == '.':
            ans += 1
        else:
            ans = 0
        if ans > k:
            print(k)
            exit(0)
    print(ans)

=======
Suggestion 4

def main():
    S = input()
    K = int(input())
    #print(S)
    #print(K)
    #print(S.find('X',0,len(S)))
    #print(S.find('X',1,len(S)))
    #print(S.find('X',2,len(S)))
    #print(S.find('X',3,len(S)))
    #print(S.find('X',4,len(S)))
    #print(S.find('X',5,len(S)))
    #print(S.find('X',6,len(S)))
    #print(S.find('X',7,len(S)))
    #print(S.find('X',8,len(S)))
    #print(S.find('X',9,len(S)))
    #print(S.find('X',10,len(S)))
    #print(S.find('X',11,len(S)))
    #print(S.find('X',12,len(S)))
    #print(S.find('X',13,len(S)))
    #print(S.find('X',14,len(S)))
    #print(S.find('X',15,len(S)))
    #print(S.find('X',16,len(S)))
    #print(S.find('X',17,len(S)))
    #print(S.find('X',18,len(S)))
    #print(S.find('X',19,len(S)))
    #print(S.find('X',20,len(S)))
    #print(S.find('X',21,len(S)))
    #print(S.find('X',22,len(S)))
    #print(S.find('X',23,len(S)))
    #print(S.find('X',24,len(S)))
    #print(S.find('X',25,len(S)))
    #print(S.find('X',26,len(S)))
    #print(S.find('X',27,len(S)))
    #print(S.find('X',28,len(S)))
    #print(S.find('X',29,len(S)))
    #print(S.find('X',30,len(S)))
    #print(S.find('X',31,len(S)))
    #print(S.find('X',32,len(S)))
    #print(S.find('X',33,len(S)))
    #print(S.find('X',34,len(S)))
    #print(S.find('X',35,len(S)))
    #print(S.find('X',36,len(S)))
    #print(S.find('X',37,len(S)))
    #print(S.find('X',38,len(S)))
    #print(S.find('X',39

=======
Suggestion 5

def main():
    S = input()
    K = int(input())
    S = S.replace('.', ' ')
    S = S.split(' ')
    S = [len(s) for s in S]
    S.sort(reverse=True)
    print(sum(S[:K]))

=======
Suggestion 6

def main():
    s = input()
    k = int(input())
    n = len(s)
    cnt = 0
    for i in range(n-1):
        if s[i] == s[i+1]:
            cnt += 1
    print(min(n-1, cnt+2*k))

=======
Suggestion 7

def main():
    s = input()
    k = int(input())
    n = len(s)
    cnt = 0
    ans = 0
    for i in range(n):
        if s[i] == 'X':
            cnt += 1
        else:
            if k > 0:
                k -= 1
                cnt += 1
            else:
                cnt = 0
        ans = max(ans, cnt)
    print(ans)

=======
Suggestion 8

def main():
    s = input()
    k = int(input())
    x = 0
    y = 0
    z = 0
    for i in range(len(s)):
        if s[i] == 'X':
            x += 1
        else:
            y = max(y, x)
            x = 0
    y = max(y, x)
    for i in range(len(s)):
        if s[i] == '.':
            z += 1
    print(min(y + k, z))

=======
Suggestion 9

def main():
    S = input()
    K = int(input())
    S = S.replace("X",".X.")
    S = S.split(".")
    ans = 0
    for s in S:
        ans = max(ans,len(s))
    print(ans-K)

=======
Suggestion 10

def solve():
    S = input()
    K = int(input())
    N = len(S)
    cnt = 0
    for i in range(N):
        if S[i] == 'X':
            cnt += 1
    if K == 0:
        print(cnt)
        return
    if cnt == N:
        print(cnt)
        return
    if cnt == N-1:
        print(cnt+1)
        return
    if cnt == N-2:
        print(cnt+2)
        return
    if cnt == N-3:
        print(cnt+3)
        return
    if cnt == N-4:
        print(cnt+4)
        return
    if cnt == N-5:
        print(cnt+5)
        return
    if cnt == N-6:
        print(cnt+6)
        return
    if cnt == N-7:
        print(cnt+7)
        return
    if cnt == N-8:
        print(cnt+8)
        return
    if cnt == N-9:
        print(cnt+9)
        return
    if cnt == N-10:
        print(cnt+10)
        return
    if cnt == N-11:
        print(cnt+11)
        return
    if cnt == N-12:
        print(cnt+12)
        return
    if cnt == N-13:
        print(cnt+13)
        return
    if cnt == N-14:
        print(cnt+14)
        return
    if cnt == N-15:
        print(cnt+15)
        return
    if cnt == N-16:
        print(cnt+16)
        return
    if cnt == N-17:
        print(cnt+17)
        return
    if cnt == N-18:
        print(cnt+18)
        return
    if cnt == N-19:
        print(cnt+19)
        return
    if cnt == N-20:
        print(cnt+20)
        return
    if cnt == N-21:
        print(cnt+21)
        return
    if cnt == N-22:
        print(cnt+22)
        return
    if cnt == N-23:
        print(cnt+23)
        return
    if cnt == N-24:
        print(cnt+24)
        return
    if cnt == N-25:
        print(cnt+25)
        return
