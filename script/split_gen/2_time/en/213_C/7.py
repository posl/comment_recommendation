def main():
    H, W, N = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N)]
    A = [a for a, b in AB]
    B = [b for a, b in AB]
    A = sorted(list(set(A)))
    B = sorted(list(set(B)))
    for a, b in AB:
        print(A.index(a) + 1, B.index(b) + 1)
