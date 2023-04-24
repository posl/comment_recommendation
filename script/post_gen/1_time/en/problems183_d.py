Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, W = map(int, input().split())
    events = []
    for _ in range(N):
        S, T, P = map(int, input().split())
        events.append((S, P))
        events.append((T, -P))
    events.sort()
    now = 0
    for _, P in events:
        now += P
        if now > W:
            print('No')
            break
    else:
        print('Yes')

=======
Suggestion 2

def main():
    N, W = map(int, input().split())
    water = [0] * 200001
    for _ in range(N):
        S, T, P = map(int, input().split())
        water[S] += P
        water[T] -= P
    for i in range(200000):
        water[i + 1] += water[i]
    print('Yes' if max(water) <= W else 'No')

=======
Suggestion 3

def main():
    N, W = map(int, input().split())
    water = [0] * 200001
    for _ in range(N):
        S, T, P = map(int, input().split())
        water[S] += P
        water[T] -= P
    for i in range(200000):
        water[i+1] += water[i]
        if water[i] > W:
            print('No')
            return
    print('Yes')
    return

=======
Suggestion 4

def main():
    N, W = map(int, input().split())
    water = [0] * 200001
    for i in range(N):
        S, T, P = map(int, input().split())
        water[S] += P
        water[T] -= P
    for i in range(200000):
        water[i + 1] += water[i]
    print('Yes' if max(water) <= W else 'No')

=======
Suggestion 5

def main():
    N, W = map(int, input().split())
    water = [0] * 200001
    for _ in range(N):
        s, t, p = map(int, input().split())
        water[s] += p
        water[t] -= p

    for i in range(200000):
        water[i + 1] += water[i]

    if max(water) > W:
        print('No')
    else:
        print('Yes')

=======
Suggestion 6

def solve():
    N, W = map(int, input().split())
    events = []
    for _ in range(N):
        s, t, p = map(int, input().split())
        events.append((s, p))
        events.append((t, -p))
    events.sort()
    now = 0
    for t, p in events:
        now += p
        if now > W:
            return "No"
    return "Yes"
print(solve())

=======
Suggestion 7

def main():
    N, W = map(int, input().split())
    A = []
    for _ in range(N):
        s, t, p = map(int, input().split())
        A.append((s, p))
        A.append((t, -p))
    A.sort()
    now = 0
    for i in range(len(A)):
        now += A[i][1]
        if now > W:
            print("No")
            return
    print("Yes")

=======
Suggestion 8

def main():
    N, W = map(int, input().split())
    water = [0 for _ in range(200001)]
    for _ in range(N):
        S, T, P = map(int, input().split())
        water[S] += P
        water[T] -= P
    for i in range(1, len(water)):
        water[i] += water[i-1]
    for w in water:
        if w > W:
            print("No")
            return
    print("Yes")

=======
Suggestion 9

def main():
    N, W = map(int, input().split())
    T = [0] * 200001
    for i in range(N):
        S, T, P = map(int, input().split())
        T[S] += P
        T[T] -= P
    for i in range(1, 200001):
        T[i] += T[i - 1]
    print("Yes" if max(T) <= W else "No")

=======
Suggestion 10

def main():
    N, W = map(int, input().split())
    # 時間ごとの使用量を記録する配列を用意
    water = [0] * 200005
    # 各人の使用量を記録
    for i in range(N):
        s, t, p = map(int, input().split())
        water[s] += p
        water[t] -= p
    # 時間ごとに使用量を計算
    for i in range(200005):
        if i == 0:
            continue
        water[i] += water[i - 1]
        if water[i] > W:
            print('No')
            return
    print('Yes')
