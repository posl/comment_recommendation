Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, M = map(int, input().split())

=======
Suggestion 2

def main():
    n,m = map(int,input().split())
    ans = "No"
    people = []
    for i in range(m):
        people.append(list(map(int,input().split())))
    for i in range(m):
        for j in range(i+1,m):
            if len(set(people[i][1:]).intersection(set(people[j][1:]))) > 0:
                ans = "Yes"
                break
    print(ans)
main()

=======
Suggestion 3

def main():
    n, m = map(int, input().split())
    a = [[0 for i in range(n)] for j in range(m)]
    for i in range(m):
        a[i] = list(map(int, input().split()))
    for i in range(m):
        for j in range(i+1, m):
            for k in range(n):
                if a[i][k] == a[j][k]:
                    print('Yes')
                    return
    print('No')
    return

=======
Suggestion 4

def get_input():
    n, m = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(m)]
    return n, m, a

=======
Suggestion 5

def main():
    n, m = map(int, input().split())
    a = [[0 for _ in range(n)] for _ in range(m)]
    for i in range(m):
        a[i] = list(map(int, input().split()))
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            for k in range(m):
                if i+1 in a[k] and j+1 in a[k]:
                    break
            else:
                print('No')
                return
    print('Yes')

=======
Suggestion 6

def main():
    n,m = map(int,input().split())
    k = [0 for i in range(m)]
    x = [[0 for j in range(n)] for i in range(m)]
    for i in range(m):
        k[i],*x[i] = map(int,input().split())
    for i in range(n):
        for j in range(n):
            if i != j:
                flag = 0
                for l in range(m):
                    if i+1 in x[l] and j+1 in x[l]:
                        flag = 1
                        break
                if flag == 0:
                    print("No")
                    return
    print("Yes")
    return

=======
Suggestion 7

def main():
    N, M = map(int, input().split())
    k = []
    x = []
    for i in range(M):
        k.append(list(map(int, input().split())))
        x.append(k[i][1:])

    for i in range(N):
        for j in range(N):
            if i != j and not any([i+1 in x[k] and j+1 in x[k] for k in range(M)]):
                print('No')
                exit()
    print('Yes')

=======
Suggestion 8

def main():
    N,M = map(int,input().split())
    k = [0]*M
    x = [0]*M
    for i in range(M):
        k[i],x[i] = map(int,input().split())
    for i in range(M):
        for j in range(i+1,M):
            if len(set(x[i]) & set(x[j])) != 0:
                print("Yes")
                return
    print("No")
    return

=======
Suggestion 9

def solve():
    N, M = map(int, input().split())
    A = [[0 for i in range(N)] for i in range(N)]
    for i in range(M):
        a = list(map(int, input().split()))
        for j in range(1, a[0]+1):
            for k in range(j+1, a[0]+1):
                A[a[j]-1][a[k]-1] = 1
    for i in range(N):
        for j in range(N):
            if A[i][j] == 0:
                print("No")
                return
    print("Yes")
    return

=======
Suggestion 10

def main():
    n,m = map(int,input().split())
    a = []
    for i in range(m):
        a.append(list(map(int,input().split())))
    for i in range(m):
        for j in range(i+1,m):
            if len(set(a[i][1:]+a[j][1:])) == n:
                print("No")
                return
    print("Yes")
main()
