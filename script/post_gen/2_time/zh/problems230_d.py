Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    pass

=======
Suggestion 2

def solve():
    pass

=======
Suggestion 3

def main():
    n,d = map(int, input().split())
    l = []
    r = []
    for i in range(n):
        a,b = map(int, input().split())
        l.append(a)
        r.append(b)

    l.sort()
    r.sort()

    ans = 0
    i = 0
    j = 0
    while i < n:
        if l[i] > r[j]:
            j += 1
        else:
            i += 1
            j += 1
            ans += 1
    print(ans)

=======
Suggestion 4

def main():
    N, D = map(int, input().split())
    L_list = []
    R_list = []
    for i in range(N):
        L, R = map(int, input().split())
        L_list.append(L)
        R_list.append(R)

    L_list.sort()
    R_list.sort()

    # print(L_list)
    # print(R_list)

    if D == 1:
        print(N)
        return

    ans = 0
    L_index = 0
    R_index = 0
    while L_index < N:
        if L_list[L_index] == R_list[R_index]:
            L_index += 1
            R_index += 1
            continue

        if L_list[L_index] < R_list[R_index]:
            ans += 1
            L_index += 1
        else:
            ans -= 1
            R_index += 1

        if ans > D:
            print(ans)
            return

    print(ans)

=======
Suggestion 5

def main():
    n,d = map(int,input().split())
    walls = []
    for i in range(n):
        walls.append(list(map(int,input().split())))
    walls.sort(key=lambda x:x[0])
    #print(walls)
    #print(n,d)
    #print(walls)
    i = 0
    j = 0
    count = 0
    while i < n:
        if j < n and walls[j][0] - walls[i][0] < d:
            count += 1
            j += 1
        else:
            count -= 1
            i += 1
    print(count)

=======
Suggestion 6

def solve(N, D, L, R):
    # print(N, D, L, R)
    # print("L", L)
    # print("R", R)
    # print("L", L)
    # print("R", R)
    # print("L", L)
    # print("R", R)
    L.sort()
    R.sort()
    # print("L", L)
    # print("R", R)
    ans = 0
    i = 0
    j = 0
    while i < N and j < N:
        if L[i] <= R[j]:
            ans += 1
            i += 1
        else:
            ans -= 1
            j += 1
    return ans

=======
Suggestion 7

def main():
    N, D = map(int, input().split())
    L = []
    R = []
    for i in range(N):
        l, r = map(int, input().split())
        L.append(l)
        R.append(r)
    L.sort()
    R.sort()
    i = 0
    j = 0
    ans = 0
    while i < N:
        if L[i] < R[j]:
            ans += 1
            i += 1
        else:
            ans -= 1
            j += 1
    print(ans)

=======
Suggestion 8

def main():
    n, d = map(int, input().split())
    lr = [list(map(int, input().split())) for _ in range(n)]
    lr.sort(key=lambda x: x[1])
    r = 0
    ans = 0
    for l, r in lr:
        if r - l + 1 <= d:
            continue
        ans += (r - l + 1 - d) // d
        if (r - l + 1 - d) % d != 0:
            ans += 1
    print(ans)
