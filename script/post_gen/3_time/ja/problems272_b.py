Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n, m = map(int, input().split())
    k = [0] * m
    x = [0] * m
    for i in range(m):
        k[i], *x[i] = map(int, input().split())
    for i in range(m):
        for j in range(i+1, m):
            for l in range(k[i]):
                for m in range(k[j]):
                    if x[i][l] == x[j][m]:
                        print("Yes")
                        return
    print("No")

=======
Suggestion 2

def main():
    N, M = map(int, input().split())
    x = []
    for i in range(M):
        x.append(list(map(int, input().split()))[1:])
    for i in range(M):
        for j in range(M):
            if i == j:
                continue
            if set(x[i]) & set(x[j]):
                print("Yes")
                return
    print("No")

=======
Suggestion 3

def main():
    n, m = map(int, input().split())
    x = [list(map(int, input().split()))[1:] for _ in range(m)]
    for i in range(m):
        x[i].sort()
    for i in range(m):
        for j in range(i+1, m):
            if x[i] == x[j]:
                print('Yes')
                return
    print('No')

=======
Suggestion 4

def main():
    N, M = map(int, input().split())
    d = {}
    for i in range(M):
        k, *x = map(int, input().split())
        for j in x:
            if j in d:
                d[j] += 1
            else:
                d[j] = 1
    print('Yes' if all(i == M for i in d.values()) else 'No')

=======
Suggestion 5

def main():
    N, M = map(int, input().split())
    ans = "No"
    for i in range(M):
        k, *x = map(int, input().split())
        if len(set(x)) != len(x):
            ans = "Yes"
    print(ans)

=======
Suggestion 6

def main():
    N, M = map(int, input().split())
    kx = []
    for i in range(M):
        kx.append(list(map(int, input().split())))
    ans = "Yes"
    for i in range(M):
        for j in range(i+1, M):
            if len(set(kx[i][1:]) & set(kx[j][1:])) == 0:
                ans = "No"
                break
    print(ans)

=======
Suggestion 7

def main():
    N, M = map(int, input().split())
    party = []
    for i in range(M):
        party.append(list(map(int, input().split())))

    for i in range(M):
        for j in range(M):
            if i == j:
                continue
            for k in range(party[i][0]):
                if party[i][k+1] in party[j]:
                    print("Yes")
                    return
    print("No")

=======
Suggestion 8

def main():
    N, M = map(int, input().split())
    x = [list(map(int, input().split())) for _ in range(M)]
    #print(N)
    #print(M)
    #print(x)
    #print(x[0][0])
    #print(x[0][1])
    #print(x[1][0])
    #print(x[1][1])
    #print(x[2][0])
    #print(x[2][1])

    for i in range(M-1):
        for j in range(i+1, M):
            #print(i, j)
            #print(x[i][0], x[j][0])
            #print(x[i][1], x[j][1])
            if x[i][0] != x[j][0] and x[i][0] != x[j][1] and x[i][1] != x[j][0] and x[i][1] != x[j][1]:
                print('No')
                exit()

    print('Yes')

=======
Suggestion 9

def main():
    n,m = map(int, input().split())
    kx = []
    for i in range(m):
        kx.append(list(map(int, input().split())))

    #print(n,m)
    #print(kx)

    flag = False
    for i in range(m):
        for j in range(i+1, m):
            #print("i,j", i,j)
            #print(kx[i])
            #print(kx[j])
            #print(set(kx[i][1:]) & set(kx[j][1:]))
            if len(set(kx[i][1:]) & set(kx[j][1:])) > 0:
                flag = True
                break
        if flag:
            break

    if flag:
        print("Yes")
    else:
        print("No")

=======
Suggestion 10

def main():
    N,M = map(int, input().split())
    kx = [list(map(int, input().split())) for _ in range(M)]
    kx = [[kx[i][j] for j in range(1, kx[i][0]+1)] for i in range(M)]
    #print(kx)
    for i in range(N):
        for j in range(i+1, N):
            if not [i+1, j+1] in kx:
                print("No")
                return
    print("Yes")
    return
