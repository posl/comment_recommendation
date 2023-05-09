def main():
    N, Q = map(int, input().split())
    follow = [False] * N
    for _ in range(Q):
        t, a, b = map(int, input().split())
        if t == 1:
            follow[a - 1] = True
        elif t == 2:
            follow[a - 1] = False
        else:
            print('Yes' if follow[a - 1] and follow[b - 1] else 'No')
