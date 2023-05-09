def main():
    H, W, N = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N)]
    A = [a for a, b in AB]
    B = [b for a, b in AB]
    A.sort()
    B.sort()
    d = {a: i for i, a in enumerate(A)}
    e = {b: i for i, b in enumerate(B)}
    for a, b in AB:
        print(d[a] + 1, e[b] + 1)
