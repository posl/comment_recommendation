Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, M = map(int, input().split())
    n = [0] * M
    x = [0] * M
    for i in range(M):
        n[i], *x[i] = map(int, input().split())
    for i in range(1, N + 1):
        for j in range(i + 1, N + 1):
            for k in range(M):
                if i in x[k] and j in x[k]:
                    break
            else:
                print("No")
                exit()
    print("Yes")
main()

=======
Suggestion 2

def get_input():
    n,m = map(int,input().split())
    return n,m

=======
Suggestion 3

def main():
    N, M = map(int, input().split())
    K = []
    for i in range(M):
        K.append(list(map(int, input().split())))

    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            for k in range(M):
                if not (i+1 in K[k][1:] and j+1 in K[k][1:]):
                    break
            else:
                continue
            break
        else:
            continue
        break
    else:
        print("Yes")
        return
    print("No")
    return

=======
Suggestion 4

def main():
    N,M = map(int,input().split())
    #print(N,M)
    X = []
    for i in range(M):
        X.append(list(map(int,input().split())))
    #print(X)
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            else:
                flag = 0
                for k in range(M):
                    if i+1 in X[k] and j+1 in X[k]:
                        flag = 1
                        break
                if flag == 0:
                    print('No')
                    return
    print('Yes')
    return

=======
Suggestion 5

def main():
    n, m = map(int, input().split())
    d = {}
    for i in range(m):
        k, *a = map(int, input().split())
        for j in range(k):
            if a[j] not in d:
                d[a[j]] = set()
            d[a[j]].add(i)
    ans = 'Yes'
    for v in d.values():
        if len(v) == 1:
            ans = 'No'
            break
    print(ans)

=======
Suggestion 6

def main():
    N, M = map(int, input().split())
    x = []
    for i in range(M):
        x.append(list(map(int, input().split())))

    # print(N,M,x)
    # print(x[0][0])

    # print(x[0][0])
    # print(x[0][1])
    # print(x[0][2])
    # print(x[1][0])
    # print(x[1][1])
    # print(x[1][2])
    # print(x[2][0])
    # print(x[2][1])
    # print(x[2][2])

    # print(x[0][0],x[0][1])
    # print(x[0][0],x[0][2])
    # print(x[0][1],x[0][2])
    # print(x[1][0],x[1][1])
    # print(x[1][0],x[1][2])
    # print(x[1][1],x[1][2])
    # print(x[2][0],x[2][1])
    # print(x[2][0],x[2][2])
    # print(x[2][1],x[2][2])

    # print(x[0][0],x[0][1])
    # print(x[0][0],x[0][2])
    # print(x[0][1],x[0][2])
    # print(x[1][0],x[1][1])
    # print(x[1][0],x[1][2])
    # print(x[1][1],x[1][2])
    # print(x[2][0],x[2][1])
    # print(x[2][0],x[2][2])
    # print(x[2][1],x[2][2])

    # print(x[0][0],x[0][1])
    # print(x[0][0],x[0][2])
    # print(x[0][1],x[0][2])
    # print(x[1][0],x[1][1])
    # print(x[1][0],x[1][2])
    # print(x[1][1],x[1][2])
    # print(x[2

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
            if i == j:
                continue
            else:
                flag = True
                for l in range(M):
                    if i + 1 not in x[l] or j + 1 not in x[l]:
                        flag = False
                if flag:
                    print("Yes")
                    exit()
    print("No")

=======
Suggestion 8

def main():
    n,m = map(int,input().split())
    a = []
    for i in range(m):
        a.append(list(map(int,input().split())))
    a.sort()
    ans = "No"
    for i in range(m-1):
        for j in range(i+1,m):
            if a[i][0] == a[j][0]:
                continue
            if a[i][1] == a[j][1]:
                ans = "Yes"
                break
    print(ans)

=======
Suggestion 9

def main():
    N,M = map(int, input().split())
    ans = [[0] * N for _ in range(N)]
    for i in range(M):
        k,x = map(int, input().split())
        for j in range(k):
            ans[x-1][int(input())-1] = 1
    for i in range(N):
        for j in range(N):
            if ans[i][j] == 0 and i != j:
                print("No")
                return
    print("Yes")

=======
Suggestion 10

def main():
    n,m=map(int,input().split())
    a=[list(map(int,input().split())) for i in range(m)]
    ans="No"
    for i in range(1,n+1):
        for j in range(i+1,n+1):
            for k in range(m):
                if i in a[k] and j in a[k]:
                    ans="Yes"
                    break
    print(ans)
