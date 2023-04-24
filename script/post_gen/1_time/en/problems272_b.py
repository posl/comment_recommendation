Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n, m = map(int, input().split())
    a = [list(map(int, input().split()))[1:] for _ in range(m)]
    for i in range(n):
        for j in range(i + 1, n):
            if not any(i + 1 in x and j + 1 in x for x in a):
                print('No')
                return
    print('Yes')

=======
Suggestion 2

def main():
    N, M = map(int, input().split())
    x = []
    for _ in range(M):
        x.append(list(map(int, input().split()))[1:])
    for i in range(N):
        for j in range(N):
            if i != j:
                if not (i+1 in x[j]):
                    print('No')
                    return
    print('Yes')
    return

=======
Suggestion 3

def solve():
    N, M = [int(x) for x in input().split()]
    A = []
    for i in range(M):
        A.append([int(x) for x in input().split()][1:])
    for i in range(M):
        for j in range(i+1, M):
            if len(set(A[i]) & set(A[j])) == 0:
                print("No")
                return
    print("Yes")

=======
Suggestion 4

def solve():
    N, M = map(int, input().split())
    A = [list(map(int, input().split()))[1:] for _ in range(M)]

    for i in range(N):
        for j in range(i+1, N):
            if not any([i+1 in a and j+1 in a for a in A]):
                return False
    return True

print('Yes' if solve() else 'No')

=======
Suggestion 5

def main():
    n, m = map(int, input().split())
    a = []
    for i in range(m):
        a.append(list(map(int, input().split())))
    ans = "No"
    for i in range(m):
        for j in range(i+1, m):
            if len(set(a[i][1:]) & set(a[j][1:])) > 0:
                ans = "Yes"
                break
    print(ans)

=======
Suggestion 6

def main():
    n, m = map(int, input().split())
    a = [set(map(int, input().split()[1:])) for _ in range(m)]
    print('YNeos'[any(a[i] & a[j] == set() for i in range(m) for j in range(i+1, m))::2])

=======
Suggestion 7

def main():
    N, M = map(int, input().split())
    parties = []
    for i in range(M):
        parties.append(list(map(int, input().split()))[1:])
    # print(parties)

    for i in range(N):
        for j in range(N):
            if i != j:
                flag = False
                for party in parties:
                    if i+1 in party and j+1 in party:
                        flag = True
                        break
                if not flag:
                    print("No")
                    exit()
    print("Yes")

=======
Suggestion 8

def main():
    N, M = map(int, input().split())
    x = [list(map(int, input().split())) for _ in range(M)]
    ans = 'Yes'
    for i in range(1, N+1):
        for j in range(i+1, N+1):
            cnt = 0
            for k in range(M):
                if i in x[k] and j in x[k]:
                    cnt += 1
            if cnt == 0:
                ans = 'No'
                break
    print(ans)
main()

=======
Suggestion 9

def main():
    N, M = map(int, input().split())
    parties = [list(map(int, input().split())) for _ in range(M)]
    people = set([i for i in range(1, N + 1)])
    for party in parties:
        people &= set(party[1:])
    print('Yes' if len(people) == N else 'No')

=======
Suggestion 10

def main():
    n,m = map(int,input().split())
    a = []
    for i in range(m):
        a.append(list(map(int,input().split())))
    #print(a)
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            else:
                #print(i,j)
                flag = 0
                for k in range(m):
                    if i+1 in a[k] and j+1 in a[k]:
                        flag = 1
                        break
                if flag == 0:
                    print('No')
                    return
    print('Yes')
