Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n, k = map(int, input().split())
    a = []
    b = []
    for i in range(n):
        ai, bi = map(int, input().split())
        a.append(ai)
        b.append(bi)
    a, b = zip(*sorted(zip(a, b), key=lambda x:x[0]))
    # print(a, b)
    ans = k
    for i in range(n):
        if a[i] > ans:
            break
        ans += b[i]
    print(ans)

=======
Suggestion 2

def main():
    N, K = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N)]
    AB.sort()
    for A, B in AB:
        if K >= A:
            K += B
    print(K)

=======
Suggestion 3

def main():
    N, K = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N)]
    AB.sort()
    money = K
    for i in range(N):
        if money < AB[i][0]:
            break
        money += AB[i][1]
    print(money)

=======
Suggestion 4

def main():
    n, k = map(int, input().split())
    friends = []
    for _ in range(n):
        friends.append(list(map(int, input().split())))
    friends.sort(key=lambda x: x[0])
    money = k
    village = 0
    for i in range(n):
        if friends[i][0] <= village:
            money += friends[i][1]
        else:
            if friends[i][0] - village > money:
                break
            else:
                money -= friends[i][0] - village
                money += friends[i][1]
                village = friends[i][0]
    print(village + money)

=======
Suggestion 5

def main():
    n,k = map(int,input().split())
    l = []
    for i in range(n):
        a,b = map(int,input().split())
        l.append([a,b])
    l.sort()
    for i in range(n):
        if k < l[i][0]:
            break
        else:
            k += l[i][1]
    print(k)

=======
Suggestion 6

def main():
    N,K = map(int,input().split())
    friends = []
    for i in range(N):
        friends.append(list(map(int,input().split())))
    friends.sort()
    # print(friends)
    for i in range(N):
        if friends[i][0] > K:
            break
        K += friends[i][1]
    print(K)

=======
Suggestion 7

def main():
    n, k = map(int, input().split())
    people = []
    for i in range(n):
        a, b = map(int, input().split())
        people.append([a, b])
    people.sort()
    i = 0
    while k > 0 and i < n:
        if k >= people[i][0]:
            k += people[i][1]
        else:
            break
        i += 1
    print(k)

=======
Suggestion 8

def find_max_village(N, K, AB):
    AB.sort(key=lambda x: x[0])
    AB.sort(key=lambda x: x[1], reverse=True)
    # print(AB)
    res = 0
    for i in range(N):
        if K >= AB[i][0]:
            K += AB[i][1]
            res = AB[i][0]
    return res

=======
Suggestion 9

def main():
    n, k = map(int, input().split())
    friends = []
    for i in range(n):
        friends.append(list(map(int, input().split())))
    friends.sort()
    # print(friends)
    money = k
    village = 0
    for i in range(n):
        if friends[i][0] > village:
            if friends[i][0] - village > money:
                break
            else:
                money += friends[i][1]
                village = friends[i][0]
    print(village + money)

=======
Suggestion 10

def solve():
    N, K = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N)]
    AB.sort()
    ans = K
    for a, b in AB:
        if a <= ans:
            ans += b
    print(ans)
