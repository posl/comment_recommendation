Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, M = map(int, input().split())
    A = []
    B = []
    for _ in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    #print(A)
    #print(B)
    AB = []
    for i in range(N):
        AB.append([A[i], B[i]])
    #print(AB)
    AB.sort()
    #print(AB)
    ans = 0
    for i in range(N):
        if M <= AB[i][1]:
            ans += AB[i][0] * M
            break
        else:
            ans += AB[i][0] * AB[i][1]
            M -= AB[i][1]
    print(ans)

=======
Suggestion 2

def main():
    N, M = map(int, input().split())
    A = []
    B = []
    for _ in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    C = list(zip(A, B))
    C.sort()
    ans = 0
    for a, b in C:
        if b <= M:
            ans += a * b
            M -= b
        else:
            ans += a * M
            break
    print(ans)

=======
Suggestion 3

def main():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N)]
    AB.sort()
    ans = 0
    for a, b in AB:
        if b <= M:
            ans += a * b
            M -= b
        else:
            ans += a * M
            break
    print(ans)

=======
Suggestion 4

def main():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N)]
    AB.sort(key=lambda x: x[0])
    ans = 0
    for a, b in AB:
        if M <= b:
            ans += a * M
            break
        else:
            ans += a * b
            M -= b
    print(ans)

=======
Suggestion 5

def main():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for i in range(N)]
    AB.sort()
    ans = 0
    for a, b in AB:
        if b <= M:
            ans += a * b
            M -= b
        else:
            ans += a * M
            break
    print(ans)

=======
Suggestion 6

def main():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N)]
    AB.sort(key=lambda x: x[0])
    money = 0
    for i in range(N):
        if M <= AB[i][1]:
            money += AB[i][0] * M
            break
        else:
            money += AB[i][0] * AB[i][1]
            M -= AB[i][1]
    print(money)

=======
Suggestion 7

def main():
    N, M = map(int, input().split())
    stores = [list(map(int, input().split())) for _ in range(N)]
    stores.sort()
    ans = 0
    for i in range(N):
        if M <= stores[i][1]:
            ans += stores[i][0] * M
            break
        else:
            ans += stores[i][0] * stores[i][1]
            M -= stores[i][1]
    print(ans)

=======
Suggestion 8

def main():
    N, M = map(int, input().split())
    a = []
    b = []
    for i in range(N):
        tmp_a, tmp_b = map(int, input().split())
        a.append(tmp_a)
        b.append(tmp_b)
    a, b = (list(t) for t in zip(*sorted(zip(a, b))))
    tmp = 0
    ans = 0
    for i in range(N):
        if tmp + b[i] <= M:
            ans += a[i] * b[i]
            tmp += b[i]
        else:
            ans += a[i] * (M - tmp)
            tmp = M
        if tmp == M:
            break
    print(ans)

=======
Suggestion 9

def main():
    N, M = map(int, input().split())
    stores = [list(map(int, input().split())) for _ in range(N)]

    stores.sort()
    ans = 0
    for i in range(N):
        if M <= stores[i][1]:
            ans += stores[i][0] * M
            break
        else:
            ans += stores[i][0] * stores[i][1]
            M -= stores[i][1]

    print(ans)

main()

=======
Suggestion 10

def main():
    # Get input
    N, M = map(int, input().split())
    A, B = [], []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    
    # Sort by price
    sort_idx = sorted(range(N), key=lambda k: A[k])
    A = [A[i] for i in sort_idx]
    B = [B[i] for i in sort_idx]
    
    # Find the minimum amount of money
    ans = 0
    for i in range(N):
        if M > B[i]:
            ans += A[i] * B[i]
            M -= B[i]
        else:
            ans += A[i] * M
            break
    
    # Output
    print(ans)
