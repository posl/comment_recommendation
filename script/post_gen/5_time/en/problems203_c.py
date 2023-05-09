Synthesizing 10/10 solutions

=======
Suggestion 1

def solve():
    n, k = map(int, input().split())
    friends = []
    for _ in range(n):
        a, b = map(int, input().split())
        friends.append((a, b))
    friends.sort()
    v = 0
    for a, b in friends:
        if a > v + k:
            break
        k -= a - v
        v = a
        k += b
    v += k
    print(v)

=======
Suggestion 2

def main():
    N, K = map(int, input().split())
    friends = []
    for i in range(N):
        A, B = map(int, input().split())
        friends.append([A, B])
    friends.sort()
    for i in range(N):
        if K < friends[i][0]:
            break
        K += friends[i][1]
    print(K)

=======
Suggestion 3

def main():
    n, k = map(int, input().split())
    ab = [list(map(int, input().split())) for _ in range(n)]
    ab.sort()
    for i in range(n):
        if k >= ab[i][0]:
            k += ab[i][1]
        else:
            print(k)
            exit()
    print(k)

=======
Suggestion 4

def problem203_c():
    n, k = map(int, input().split())
    d = dict()
    for i in range(n):
        a, b = map(int, input().split())
        if a not in d:
            d[a] = 0
        d[a] += b
    l = sorted(d.items())
    for i in range(len(l)):
        if k >= l[i][0]:
            k += l[i][1]
        else:
            print(k)
            return
    print(k)
    return

=======
Suggestion 5

def main():
    N, K = map(int, input().split())
    friends = []
    for _ in range(N):
        friends.append(list(map(int, input().split())))
    friends.sort(key=lambda x: x[0])
    i = 0
    while K > 0:
        K -= 1
        K += friends[i][1]
        i += 1
    print(friends[i-1][0])

=======
Suggestion 6

def main():
    N, K = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N)]
    AB.sort(key=lambda x: x[0])

    for a, b in AB:
        if K < a:
            break
        K += b

    print(K)

=======
Suggestion 7

def main():
    N,K = map(int, input().split())
    friends = []
    for i in range(N):
        A,B = map(int, input().split())
        friends.append([A,B])
    friends.sort()
    i = 0
    while K > 0 and i < N:
        if friends[i][0] <= K:
            K += friends[i][1]
            i += 1
        else:
            break
    print(K)
main()

=======
Suggestion 8

def main():
    N, K = map(int, input().split())
    #print(N, K)
    A = []
    B = []
    for n in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    #print(A)
    #print(B)
    money = K
    village = 0
    while money > 0:
        #print(money, village)
        for n in range(N):
            if A[n] == village:
                money += B[n]
        village += 1
        money -= 1
    print(village - 1)

=======
Suggestion 9

def main():
    #input
    n,k = map(int, input().split())
    a = []
    b = []
    for i in range(n):
        a_i, b_i = map(int, input().split())
        a.append(a_i)
        b.append(b_i)

    #compute
    village = 0
    money = k
    for i in range(n):
        if a[i] > village:
            break
        else:
            money += b[i]
            village = a[i]
    village += money

    #output
    print(village)

=======
Suggestion 10

def solve(n, k, arr):
    arr.sort()
    for i in range(n):
        if k >= arr[i][0]:
            k += arr[i][1]
        else:
            return k
    return k + arr[n-1][1]
