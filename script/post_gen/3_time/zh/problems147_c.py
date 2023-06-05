Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def check_honesty(N, A, x, y):
    honest = [0] * N
    for i in range(0, N):
        if (A[i] == 0):
            honest[i] = 1
            continue
        for j in range(0, A[i]):
            if (y[i][j] == 1):
                honest[x[i][j] - 1] = 1
    return sum(honest)

N = int(input())
A = [0] * N
x = [0] * N
y = [0] * N
for i in range(0, N):
    A[i] = int(input())
    x[i] = [0] * A[i]
    y[i] = [0] * A[i]
    for j in range(0, A[i]):
        x[i][j], y[i][j] = map(int, input().split())
print(check_honesty(N, A, x, y))

=======
Suggestion 2

def solve():
    pass

=======
Suggestion 3

def main():
    # N = 3
    # A = [1,1,1]
    # x = [[2],[1],[2]]
    # y = [[1],[1],[0]]
    N = int(input())
    A = []
    x = []
    y = []
    for i in range(N):
        A.append(int(input()))
        x.append([])
        y.append([])
        for j in range(A[i]):
            x[i].append(0)
            y[i].append(0)
        for j in range(A[i]):
            x[i][j], y[i][j] = map(int, input().split())
    # print(N, A, x, y)
    ans = 0
    for i in range(2**N):
        honest = [0] * N
        for j in range(N):
            if (i >> j) & 1:
                honest[j] = 1
        flag = True
        for j in range(N):
            if honest[j] == 1:
                for k in range(A[j]):
                    if honest[x[j][k]-1] != y[j][k]:
                        flag = False
        if flag:
            ans = max(ans, sum(honest))
    print(ans)

=======
Suggestion 4

def dfs(i, n, a, x, y):
    if i == n:
        return 0
    ans = 0
    for j in range(a[i]):
        if y[i][j] == 1:
            ans = max(ans, dfs(i+1, n, a, x, y) + 1)
        else:
            ans = max(ans, dfs(i+1, n, a, x, y))
    return ans

=======
Suggestion 5

def check_honesty(honest_list, N, A, xy_list):
    for i in range(N):
        if honest_list[i] == 1:
            for j in range(A[i]):
                if honest_list[xy_list[i][j][0]-1] != xy_list[i][j][1]:
                    return False
    return True

=======
Suggestion 6

def main():
    pass

=======
Suggestion 7

def get_honest_person_count(N, A, xy):
    honest_person_count = 0
    for i in range(2**N):
        honest_person = []
        for j in range(N):
            if ((i >> j) & 1):
                honest_person.append(j + 1)
        if len(honest_person) <= honest_person_count:
            continue
        for k in range(len(honest_person)):
            for l in range(A[honest_person[k] - 1]):
                if xy[honest_person[k] - 1][l][1] == 0 and xy[honest_person[k] - 1][l][0] in honest_person:
                    break
            else:
                if k == len(honest_person) - 1:
                    honest_person_count = len(honest_person)
                    break
                else:
                    continue
            break
    return honest_person_count

N = int(input())
A = []
xy = []
for i in range(N):
    A.append(int(input()))
    xy.append([])
    for j in range(A[i]):
        xy[i].append(list(map(int, input().split())))
print(get_honest_person_count(N, A, xy))

=======
Suggestion 8

def get_persons(n):
    return [i for i in range(1, n+1)]

=======
Suggestion 9

def get_ans(N, A, xy):
    ans = 0
    for i in range(2**N):
        b = [0]*N
        for j in range(N):
            if ((i>>j)&1):
                b[j] = 1
        flag = 1
        for j in range(N):
            if b[j] == 1:
                for k in range(A[j]):
                    if b[xy[j][k][0]-1] != xy[j][k][1]:
                        flag = 0
                        break
                if flag == 0:
                    break
        if flag == 1:
            ans = max(ans, sum(b))
    return ans
