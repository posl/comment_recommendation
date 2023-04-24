Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n, w = map(int, input().split())
    events = []
    for _ in range(n):
        s, t, p = map(int, input().split())
        events.append((s, p))
        events.append((t, -p))
    events.sort()
    water = 0
    for t, p in events:
        water += p
        if water > w:
            print("No")
            return
    print("Yes")

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
    if max(water) > W:
        print("No")
    else:
        print("Yes")

=======
Suggestion 3

def main():
    N, W = map(int, input().split())
    water = [0] * 200001
    for _ in range(N):
        S, T, P = map(int, input().split())
        water[S] += P
        water[T] -= P
    for i in range(1, 200001):
        water[i] += water[i - 1]
        if water[i] > W:
            print("No")
            return
    print("Yes")

=======
Suggestion 4

def main():
    N, W = map(int, input().split())
    usage = [0] * 200001
    for i in range(N):
        S, T, P = map(int, input().split())
        usage[S] += P
        usage[T] -= P
    for i in range(1, 200001):
        usage[i] += usage[i - 1]
        if usage[i] > W:
            print("No")
            return
    print("Yes")

=======
Suggestion 5

def main():
    N, W = map(int, input().split())
    time = [0] * (2 * 10 ** 5 + 1)
    for _ in range(N):
        S, T, P = map(int, input().split())
        time[S] += P
        time[T] -= P
    for i in range(1, len(time)):
        time[i] += time[i - 1]
    if max(time) > W:
        print('No')
    else:
        print('Yes')
main()

=======
Suggestion 6

def main():
    N, W = map(int, input().split())
    diff = [0] * 200002
    for i in range(N):
        S, T, P = map(int, input().split())
        diff[S] += P
        diff[T] -= P
    for i in range(1, 200002):
        diff[i] += diff[i - 1]
    if max(diff) <= W:
        print('Yes')
    else:
        print('No')

=======
Suggestion 7

def main():
    N, W = list(map(int, input().split()))
    water = [0] * 200001
    for _ in range(N):
        s, t, p = list(map(int, input().split()))
        water[s] += p
        water[t] -= p
    for i in range(1, len(water)):
        water[i] += water[i - 1]
        if water[i] > W:
            print('No')
            exit()
    print('Yes')

=======
Suggestion 8

def main():
    N, W = map(int, input().split())
    P = [list(map(int, input().split())) for _ in range(N)]
    P.sort(key=lambda x:x[1])
    ans = "Yes"
    for i in range(N):
        if P[i][2] > W:
            ans = "No"
            break
        W -= P[i][2]
        for j in range(i+1, N):
            if P[i][1] <= P[j][0]:
                break
            if P[i][1] < P[j][1]:
                P[j][2] -= min(P[j][2], P[i][2])
        if W == 0:
            break
    print(ans)

=======
Suggestion 9

def main():
    N, W = map(int, input().split())
    # N: Number of people
    # W: Water heater capacity
    # S_i: Start time
    # T_i: End time
    # P_i: Water usage
    # T: Total water usage
    T = [0] * 200001
    for i in range(N):
        S, T, P = map(int, input().split())
        T[S] += P
        T[T] -= P
    for i in range(200000):
        T[i + 1] += T[i]
    for i in range(200000):
        if T[i] > W:
            print("No")
            return
    print("Yes")
    return

=======
Suggestion 10

def main():
    n, w = map(int, input().split())
    # 1分間にどれだけの水が使われているかを記録する
    water = [0] * (200000 + 1)
    for i in range(n):
        s, t, p = map(int, input().split())
        water[s] += p
        water[t] -= p
    # 1分間にどれだけの水が使われているかを累積和で求める
    for i in range(1, 200000 + 1):
        water[i] += water[i - 1]
    # 1分間にどれだけの水が使われているかを確認する
    for i in range(1, 200000 + 1):
        if water[i] > w:
            print("No")
            return
    print("Yes")
