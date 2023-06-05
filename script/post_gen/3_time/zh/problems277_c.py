Synthesizing 10/10 solutions

=======
Suggestion 1

def check(a, b):
    if a == b:
        return True
    elif a > b:
        return False
    else:
        return True

n = int(input())
l = []
for i in range(n):
    a, b = map(int, input().split())
    l.append([a, b])
l.sort(key=lambda x: x[1])

ans = 1
for i in range(n):
    if check(ans, l[i][0]):
        ans = l[i][1]
    else:
        pass
print(ans)

=======
Suggestion 2

def main():
    n = int(input())
    ab = []
    for i in range(n):
        a,b = map(int, input().split())
        ab.append([a,b])
    ab.sort(key=lambda x:x[1])
    #print(ab)
    ans = 0
    for i in range(n):
        if i == 0:
            ans = ab[i][1]
            continue
        if ab[i][0] <= ans:
            continue
        ans = ab[i][1]
    print(ans)

=======
Suggestion 3

def main():
    N = int(input())
    AB = []
    for i in range(N):
        AB.append(list(map(int, input().split())))
    AB.sort(key=lambda x: x[1])
    #print(AB)
    #print(AB[0][1])
    for i in range(N-1):
        if AB[i][1] < AB[i+1][0]:
            print(AB[i][1])
            exit()
    print(AB[-1][1])

=======
Suggestion 4

def main():
    N = int(input())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)

    min = 1
    max = 10**9
    for i in range(N):
        if A[i] > min:
            min = A[i]
        if B[i] < max:
            max = B[i]
    if min <= max:
        print(max)
    else:
        print(0)

=======
Suggestion 5

def main():
    n = int(input())
    a, b = [], []
    for i in range(n):
        ai, bi = map(int, input().split())
        a.append(ai)
        b.append(bi)
    a.sort()
    b.sort()
    if n%2 == 0:
        x = n//2
        y = x-1
        print(b[y]-a[x]+1)
    else:
        x = n//2
        print(b[x]-a[x]+1)

=======
Suggestion 6

def get_max_floor(n, ladders):
    # 从最低层开始，逐层检查是否能到达最高层
    # 1. 如果最低层没有梯子，则不可能到达最高层
    # 2. 如果最低层有梯子，则到达最高层的条件是：
    # 2.1. 梯子的上端点等于最高层
    # 2.2. 梯子的上端点不等于最高层，且梯子的上端点能到达最高层
    # 2.3. 梯子的下端点等于最高层，且梯子的下端点能到达最高层
    # 2.4. 梯子的下端点等于最高层，且梯子的上端点能到达最高层
    # 2.5. 梯子的上端点等于最高层，且梯子的下端点能到达最高层
    # 2.6. 梯子的上端点和下端点都不等于最高层，且梯子的上端点能到达最高层，且梯子的下端点能到达最高层
    # 3. 如果最低层有多个梯子，则逐个检查是否能到达最高层
    # 4. 如果最低层没有梯子，则不可能到达最高层
    # 5. 如果最低层有梯子，则到达最高层的条件是：
    # 5.1. 梯子的上端点等于最高层
    # 5.2. 梯子的上端点不等于最高层，且梯子的上端点能到达最高层
    # 5.3. 梯子的下端点等于

=======
Suggestion 7

def main():
    N = int(input())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    A.sort()
    B.sort()
    if N % 2 == 0:
        a = A[N//2-1] + A[N//2]
        b = B[N//2-1] + B[N//2]
        print(b-a+1)
    else:
        a = A[N//2]
        b = B[N//2]
        print(b-a+1)

=======
Suggestion 8

def main():
    N = int(input())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    A.sort()
    B.sort()
    if N%2 == 0:
        a = A[int(N/2)-1] + A[int(N/2)]
        b = B[int(N/2)-1] + B[int(N/2)]
        print(int((b-a)/2+1))
    else:
        a = A[int(N/2)]
        b = B[int(N/2)]
        print(int(b-a+1))

=======
Suggestion 9

def main():
    N = int(input())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    A.sort()
    B.sort()
    if N % 2 == 1:
        print(B[N//2]-A[N//2]+1)
    else:
        print((B[N//2-1]+B[N//2])-(A[N//2-1]+A[N//2])+1)

=======
Suggestion 10

def main():
    N = int(input())
    AB = []
    for _ in range(N):
        AB.append(list(map(int, input().split())))
    AB.sort(key=lambda x: x[1])

    ans = 1
    for i in range(N):
        if ans < AB[i][0]:
            ans = AB[i][1]
    print(ans)
