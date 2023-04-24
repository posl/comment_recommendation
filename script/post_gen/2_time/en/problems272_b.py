Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, M = map(int, input().split())
    parties = [set(map(int, input().split()[1:])) for _ in range(M)]

    for i in range(N):
        for j in range(i + 1, N):
            for party in parties:
                if i + 1 in party and j + 1 in party:
                    break
            else:
                print('No')
                return

    print('Yes')

=======
Suggestion 2

def main():
    N, M = map(int, input().split())
    party = [set(map(int, input().split()[1:])) for _ in range(M)]
    for i in range(M):
        for j in range(i + 1, M):
            if len(party[i] & party[j]) == 0:
                print("No")
                return
    print("Yes")

=======
Suggestion 3

def main():
    N, M = map(int, input().split())
    party = []
    for i in range(M):
        x = list(map(int, input().split()))
        party.append(x[1:])
    for i in range(N):
        for j in range(i + 1, N):
            flag = False
            for k in party:
                if i + 1 in k and j + 1 in k:
                    flag = True
                    break
            if not flag:
                print("No")
                return
    print("Yes")

=======
Suggestion 4

def main():
    N, M = map(int, input().split())
    A = [0] * N
    for _ in range(M):
        *x, = map(int, input().split())
        for i in range(1, x[0]+1):
            A[x[i]-1] += 1
    if A.count(0) == 0:
        print("Yes")
    else:
        print("No")

main()

=======
Suggestion 5

def main():
    n, m = map(int, input().split())
    people = [[] for i in range(n)]
    for i in range(m):
        k, *x = map(int, input().split())
        for j in x:
            people[j-1].append(i)
    for i in range(n):
        people[i] = set(people[i])
    for i in range(n):
        for j in range(i+1, n):
            if people[i] & people[j] == set():
                print('No')
                return
    print('Yes')

=======
Suggestion 6

def solve():
    N, M = map(int, input().split())
    for i in range(M):
        input()
    if M == N - 1:
        print('Yes')
    else:
        print('No')

=======
Suggestion 7

def main():
    N, M = map(int, input().split())
    for i in range(M):
        input() # k_i
        if len(set(input().split())) == N:
            print('No')
            return
    print('Yes')

=======
Suggestion 8

def solve(N, M, k, x):
    #N: number of people
    #M: number of parties
    #k: k[i] is the number of people who attended the i-th party
    #x: x[i][j] is the j-th person who attended the i-th party
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            for k_i in range(M):
                if i+1 in x[k_i] and j+1 in x[k_i]:
                    break
            else:
                return 'No'
    return 'Yes'

=======
Suggestion 9

def main():
    N, M = map(int, input().split())

    # 2次元配列を宣言
    attended_party = [[0 for i in range(N)] for j in range(N)]

    for i in range(M):
        k = list(map(int, input().split()))
        for j in range(1, k[0]):
            attended_party[k[j]-1][k[j+1]-1] = 1
            attended_party[k[j+1]-1][k[j]-1] = 1

    for i in range(N):
        if 0 in attended_party[i]:
            print("No")
            return

    print("Yes")

=======
Suggestion 10

def main():
    N, M = map(int, input().split())
    # 1,2,...,N
    # N = 4
    # 1,2,3,4
    # 0,1,2,3
    # 1,2,3,4,5,6,7,8,9
    # 0,1,2,3,4,5,6,7,8
    # 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20
    # 0,1,2,3,4,5,6,7,8, 9,10,11,12,13,14,15,16,17,18,19
    # 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20
    # 0,1,2,3,4,5,6,7,8, 9,10,11,12,13,14,15,16,17,18,19
    # 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20
    # 0,1,2,3,4,5,6,7,8, 9,10,11,12,13,14,15,16,17,18,19
    # 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20
    # 0,1,2,3,4,5,6,7,8, 9,10,11,12,13,14,15,16,17,18,19
    # 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20
    # 0,1,2,3,4,5
