Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n, m = map(int, input().split())
    x = []
    for i in range(m):
        x.append(list(map(int, input().split()))[1:])
    for i in range(n):
        for j in range(i+1, n):
            if not any([i+1 in xi for xi in x]):
                print("No")
                return
    print("Yes")

=======
Suggestion 2

def main():
    N, M = map(int, input().split())
    parties = []
    for i in range(M):
        parties.append(list(map(int, input().split()))[1:])
    for i in range(N):
        for j in range(i+1, N):
            if not (i+1 in parties[j] and j+1 in parties[i]):
                print("No")
                return
    print("Yes")

=======
Suggestion 3

def main():
    N, M = map(int, input().split())
    party = []
    for i in range(M):
        party.append(list(map(int, input().split()))[1:])
    for i in range(N):
        for j in range(N):
            if i==j:
                continue
            for k in range(M):
                if i+1 in party[k] and j+1 in party[k]:
                    break
            else:
                print('No')
                return
    print('Yes')

=======
Suggestion 4

def main():
    N, M = map(int, input().split())
    party = []
    for i in range(M):
        party.append(list(map(int, input().split()))[1:])

    for i in range(N):
        for j in range(i+1, N):
            if not any([i+1 in p and j+1 in p for p in party]):
                print("No")
                return
    print("Yes")

=======
Suggestion 5

def main():
    n,m = map(int,input().split())
    k = [0]*m
    x = [0]*m
    for i in range(m):
        k[i],*x[i] = map(int,input().split())
    for i in range(n):
        for j in range(i+1,n):
            if i+1 not in x and j+1 not in x:
                print('No')
                exit()
    print('Yes')

=======
Suggestion 6

def main():
    N, M = map(int, input().split())
    A = []
    for i in range(M):
        A.append(list(map(int, input().split())))
    B = []
    for i in range(M):
        B.append(A[i][1:])
    C = []
    for i in range(M):
        for j in range(len(B[i])):
            C.append(B[i][j])
    D = set(C)
    if len(D) == N:
        print("Yes")
    else:
        print("No")

=======
Suggestion 7

def main():
    N, M = map(int, input().split())
    parties = []
    for _ in range(M):
        parties.append(list(map(int, input().split()))[1:])
    parties = sorted(parties, key=lambda x: len(x))
    for i in range(len(parties)):
        for j in range(i+1, len(parties)):
            if len(set(parties[i]+parties[j])) == N:
                print('No')
                return
    print('Yes')

=======
Suggestion 8

def main():
    N,M = map(int,input().split())
    A = []
    for _ in range(M):
        A.append(list(map(int,input().split()))[1:])
    flag = True
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            else:
                tmp = False
                for k in range(M):
                    if i+1 in A[k] and j+1 in A[k]:
                        tmp = True
                        break
                if not tmp:
                    flag = False
                    break
    if flag:
        print("Yes")
    else:
        print("No")

=======
Suggestion 9

def main():
    n,m = map(int,input().split())
    party = []
    for i in range(m):
        party.append(list(map(int,input().split())))
    party.sort()
    for i in range(m):
        for j in range(i+1,m):
            if len(set(party[i][1:]+party[j][1:])) == n:
                print("NO")
                return
    print("YES")
    return

=======
Suggestion 10

def main():
    n,m = map(int,input().split())
    a = []
    for i in range(m):
        a.append(list(map(int,input().split())))
    #print(a)
    people = []
    for i in range(n):
        people.append(i+1)
    #print(people)
    for i in range(m):
        for j in range(a[i][0]):
            if a[i][j+1] in people:
                people.remove(a[i][j+1])
    #print(people)
    if len(people) == 0:
        print('Yes')
    else:
        print('No')
