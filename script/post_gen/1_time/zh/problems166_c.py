Synthesizing 10/10 solutions

=======
Suggestion 1

def get_input():
    n,m = map(int, input().split())
    h = list(map(int, input().split()))
    ab = [list(map(int, input().split())) for _ in range(m)]
    return n,m,h,ab

=======
Suggestion 2

def main():
    N, M = map(int, input().split())
    H = list(map(int, input().split()))
    road = [list(map(int, input().split())) for _ in range(M)]
    good = [1] * N
    for i in range(M):
        if H[road[i][0]-1] <= H[road[i][1]-1]:
            good[road[i][0]-1] = 0
        if H[road[i][0]-1] >= H[road[i][1]-1]:
            good[road[i][1]-1] = 0
    print(sum(good))

=======
Suggestion 3

def get_input():
    n, m = map(int, input().split())
    h_list = list(map(int, input().split()))
    ab_list = []
    for i in range(m):
        ab_list.append(list(map(int, input().split())))
    return n, m, h_list, ab_list

=======
Suggestion 4

def main():
    pass

=======
Suggestion 5

def main():
    n,m = map(int,input().split())
    h = list(map(int,input().split()))
    a = [0]*m
    b = [0]*m
    for i in range(m):
        a[i],b[i] = map(int,input().split())
    for i in range(m):
        if h[a[i]-1] <= h[b[i]-1]:
            h[a[i]-1] = 0
        if h[b[i]-1] <= h[a[i]-1]:
            h[b[i]-1] = 0
    print(h.count(0))

=======
Suggestion 6

def problems166_c():
    N, M = map(int, input().split())
    H = list(map(int, input().split()))
    AB = [list(map(int, input().split())) for _ in range(M)]
    # print(N, M)
    # print(H)
    # print(AB)

    # 1. 首先，我们需要一个列表来存储每个观测站的海拔高度。
    # 2. 然后，我们需要一个列表来存储每个观测站的连接观测站的列表。
    # 3. 然后，我们需要一个列表来存储每个观测站是否是好的。
    # 4. 然后，我们需要一个循环来检查每个观测站是否是好的。
    # 5. 然后，我们需要一个循环来检查每个观测站是否是好的。
    # 6. 然后，我们需要一个循环来检查每个观测站是否是好的。
    # 7. 然后，我们需要一个循环来检查每个观测站是否是好的。
    # 8. 然后，我们需要一个循环来检查每个观测站是否是好的。
    # 9. 然后，我们需要一个循环来检查每个观测站是否是好的。
    # 10. 然后，我们需要一个循环来检查每个观测站是否是好的。
    # 11. 然后，我们需要一个循环来检查每个观测站是否是好的。
    # 12. 然后，我们需要一个循环来检查每个观测站是否是好的。
    # 13. 然后，我们需要一个循环来检查每个观测站是否是好的。
    # 14. 然后，我们需要一个循环来检查每个观测站是否是好的

=======
Suggestion 7

def main():
    N, M = map(int, input().split())
    H = list(map(int, input().split()))
    A = [0] * M
    B = [0] * M
    for i in range(M):
        A[i], B[i] = map(int, input().split())

    ans = 0
    for i in range(N):
        flag = True
        for j in range(M):
            if i == A[j] - 1:
                if H[i] <= H[B[j] - 1]:
                    flag = False
            elif i == B[j] - 1:
                if H[i] <= H[A[j] - 1]:
                    flag = False
        if flag:
            ans += 1
    print(ans)

=======
Suggestion 8

def main():
    N, M = map(int, input().split())
    H = list(map(int, input().split()))
    A = [0] * M
    B = [0] * M
    for i in range(M):
        A[i], B[i] = map(int, input().split())

    ans = 0
    for i in range(N):
        flag = True
        for j in range(M):
            if A[j] == i + 1:
                if H[i] <= H[B[j] - 1]:
                    flag = False
                    break
            elif B[j] == i + 1:
                if H[i] <= H[A[j] - 1]:
                    flag = False
                    break
        if flag:
            ans += 1

    print(ans)

=======
Suggestion 9

def main():
    N, M = map(int, input().split())
    H = list(map(int, input().split()))
    A = []
    B = []
    for i in range(M):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    #print(N, M, H, A, B)

    #print(N, M, H, A, B)
    #print('N = ', N)
    #print('M = ', M)
    #print('H = ', H)
    #print('A = ', A)
    #print('B = ', B)
    #print('len(H) = ', len(H))
    #print('len(A) = ', len(A))
    #print('len(B) = ', len(B))
    #print('len(H) = ', len(H))
    #print('len(A) = ', len(A))
    #print('len(B) = ', len(B))

    #print('len(H) = ', len(H))
    #print('len(A) = ', len(A))
    #print('len(B) = ', len(B))
    #print('len(H) = ', len(H))
    #print('len(A) = ', len(A))
    #print('len(B) = ', len(B))
    #print('len(H) = ', len(H))
    #print('len(A) = ', len(A))
    #print('len(B) = ', len(B))
    #print('len(H) = ', len(H))
    #print('len(A) = ', len(A))
    #print('len(B) = ', len(B))
    #print('len(H) = ', len(H))
    #print('len(A) = ', len(A))
    #print('len(B) = ', len(B))
    #print('len(H) = ', len(H))
    #print('len(A) = ', len(A))
    #print('len(B) = ', len(B))
    #print('len(H) = ', len(H))
    #print('len(A) = ', len(A))
    #print('len(B) = ', len(B))
    #print('len(H) = ', len(H))
    #print('len(A) = ', len(A))
    #print('len(B) = ', len(B))
    #print('len(H)

=======
Suggestion 10

def problems166_c():
    pass
