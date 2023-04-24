Synthesizing 10/10 solutions

=======
Suggestion 1

def solve():
    N, K = map(int, input().split())
    friends = []
    for _ in range(N):
        A, B = map(int, input().split())
        friends.append((A, B))
    friends.sort()
    money = K
    village = 0
    for A, B in friends:
        if A <= village:
            money += B
        else:
            break
    village += money
    print(village)

=======
Suggestion 2

def main():
    N, K = map(int, input().split())
    friends = []
    for i in range(N):
        a, b = map(int, input().split())
        friends.append((a, b))
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
    friends = []
    for i in range(n):
        a, b = map(int, input().split())
        friends.append((a, b))

    friends.sort(key=lambda x: x[0])

    money = k
    village = 0
    for friend in friends:
        if money >= friend[0] - village:
            money += friend[1] - (friend[0] - village)
            village = friend[0]
        else:
            break

    village += money

    print(village)

=======
Suggestion 4

def main():
  N, K = map(int, input().split())
  friends = []
  for i in range(N):
    A, B = map(int, input().split())
    friends.append((A, B))
  friends.sort()
  for friend in friends:
    if friend[0] > K:
      break
    K += friend[1]
  print(K)

=======
Suggestion 5

def solve():
    N, K = map(int, input().split())
    AB = [tuple(map(int, input().split())) for _ in range(N)]
    AB.sort()
    for A, B in AB:
        if K >= A:
            K += B
    print(K)

=======
Suggestion 6

def solve():
    N, K = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N)]
    AB.sort()
    for A, B in AB:
        if K < A:
            break
        K += B
    print(K)
solve()

=======
Suggestion 7

def main():
    N, K = map(int, input().split())
    ab = [list(map(int, input().split())) for _ in range(N)]
    ab.sort()
    for a, b in ab:
        if a > K:
            break
        K += b
    print(K)

=======
Suggestion 8

def main():
    n, k = map(int, input().split())
    ab = [list(map(int, input().split())) for _ in range(n)]
    ab.sort()
    i = 0
    while k > 0 and i < n:
        if ab[i][0] - 1 > k:
            break
        else:
            k += ab[i][1] - 1
        i += 1
    print(k + 1)

=======
Suggestion 9

def main():
    N, K = map(int, input().split())
    friend = [list(map(int, input().split())) for _ in range(N)]
    friend.sort()
    for f in friend:
        if K >= f[0]:
            K += f[1]
    print(K)

=======
Suggestion 10

def print_debug(*args):
    print(args)
