Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, K = map(int, input().split())
    P = [list(map(int, input().split())) for _ in range(N)]
    P.sort(key=lambda x: x[2], reverse=True)
    P.sort(key=lambda x: x[1], reverse=True)
    P.sort(key=lambda x: x[0], reverse=True)
    P_4 = [p[0] for p in P]
    P_4.sort(reverse=True)
    # print(P_4)
    for p in P:
        if p[0] >= P_4[K-1]:
            print('Yes')
        else:
            print('No')

=======
Suggestion 2

def readinput():
    n,k = map(int, input().split())
    p=[]
    for i in range(n):
        p.append(list(map(int, input().split())))
    return n,k,p

=======
Suggestion 3

def main():
    N, K = map(int, input().split())
    P = [list(map(int, input().split())) for _ in range(N)]
    P.sort(key=lambda x: sum(x), reverse=True)
    for i in range(N):
        if i < K:
            print('Yes')
        else:
            print('No')

=======
Suggestion 4

def main():
    n, k = map(int, input().split())
    p = [list(map(int, input().split())) for _ in range(n)]
    p = sorted(p, key=lambda x: (x[0] + x[1] + x[2], x[0], x[1], x[2]), reverse=True)
    for i in range(n):
        if i < k:
            print("Yes")
        else:
            print("No")
    return

=======
Suggestion 5

def main():
    n,k = map(int,input().split())
    p = []
    for i in range(n):
        p.append(list(map(int,input().split())))
    for i in range(n):
        p[i].sort(reverse=True)
        if sum(p[i][:3]) >= k:
            print('Yes')
        else:
            print('No')

=======
Suggestion 6

def is_top_k(n, k, p):
    #p.sort(key=lambda x:x[0]+x[1]+x[2], reverse=True)
    p.sort(reverse=True)
    #print(p)
    for i in range(n):
        if i < k:
            if p[i][0]+p[i][1]+p[i][2] < p[k-1][0]+p[k-1][1]+p[k-1][2]:
                return 'No'
    return 'Yes'

=======
Suggestion 7

def check(n,k,ps):
    s = sorted(ps, reverse=True)
    if s[0] <= s[k-1]:
        return False
    else:
        return True

=======
Suggestion 8

def main():
    N, K = map(int, input().split())
    P = [list(map(int, input().split())) for _ in range(N)]
    res = ['Yes' for _ in range(N)]

    for i in range(N):
        for j in range(i):
            if P[j][0] + P[j][1] + P[j][2] > P[i][0] + P[i][1] + P[i][2]:
                res[i] = 'No'
                break
    for i in range(N):
        for j in range(i):
            if P[j][0] + P[j][1] > P[i][0] + P[i][1]:
                res[i] = 'No'
                break
    for i in range(N):
        for j in range(i):
            if P[j][0] > P[i][0]:
                res[i] = 'No'
                break
    print('\n'.join(res))

=======
Suggestion 9

def main():
    n, k = map(int, input().split())
    score = []
    for i in range(n):
        score.append(sum(list(map(int, input().split()))))
    score.sort(reverse=True)
    print("Yes" if score[k-1] > score[k] else "No")

=======
Suggestion 10

def main():
    n,k = map(int,input().split())
    p = []
    for i in range(n):
        p.append(list(map(int,input().split())))

    for i in range(n):
        if sum(p[i]) + 300 > sum(p[k-1]):
            print('Yes')
        else:
            print('No')
main()
