Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n, m = map(int, input().split())
    k = []
    a = []
    for i in range(n):
        ki, ai = map(int, input().split())
        k.append(ki)
        a.append(ai)
    #print(n, m)
    #print(k)
    #print(a)
    food = [0] * m
    for i in range(n):
        for j in range(k[i]):
            food[a[i][j] - 1] += 1
    #print(food)
    print(food.count(n))

=======
Suggestion 2

def main():
    N, M = map(int, input().split())
    A = [list(map(int, input().split()))[1:] for _ in range(N)]
    print(len(set.intersection(*map(set, A))))

=======
Suggestion 3

def main():
    n, m = map(int, input().split())
    a = []
    for i in range(n):
        a.append(list(map(int, input().split())))

    count = 0
    for i in range(1, m+1):
        for j in range(n):
            if i in a[j][1:]:
                if j == n-1:
                    count += 1
                    break
                else:
                    continue
            else:
                break

    print(count)

=======
Suggestion 4

def main():
    n,m = map(int, input().split())
    a = []
    for i in range(n):
        a.append(list(map(int, input().split()))[1:])
    count = 0
    for i in range(1,m+1):
        flg = True
        for j in range(n):
            if i not in a[j]:
                flg = False
        if flg:
            count += 1
    print(count)

=======
Suggestion 5

def main():
    N, M = map(int, input().split())
    ans = [0] * M
    for _ in range(N):
        *A, = map(int, input().split())
        for a in A:
            ans[a-1] += 1
    print(ans.count(N))

=======
Suggestion 6

def main():
    n,m = map(int,input().split())
    a = []
    for i in range(n):
        a.append(list(map(int,input().split()))[1:])
    ans = 0
    for i in range(m):
        for j in range(n):
            if not i+1 in a[j]:
                break
        else:
            ans += 1
    print(ans)
    return

=======
Suggestion 7

def main():
    N, M = map(int, input().split())
    count = 0
    for i in range(N):
        K, *A = map(int, input().split())
        if len(set(A)) == len(A):
            count += 1
    print(count)

=======
Suggestion 8

def main():
    N,M = map(int,input().split())
    A = [list(map(int,input().split())) for i in range(N)]
    A = [a[1:] for a in A]
    A = set(A[0]).intersection(*A)
    print(len(A))

=======
Suggestion 9

def getints(): return list(map(int, input().split()))
n,m=getints()
a=[]
for i in range(n):
    a.append(set(getints()[1:]))
print(len(set.intersection(*a)))

=======
Suggestion 10

def get_list_from_line():
    return list(map(int, input().split()))
