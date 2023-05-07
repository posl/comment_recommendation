def main():
    N = int(input())
    S = []
    T = []
    for _ in range(N):
        a, b = map(int, input().split())
        S.append((a, b))
    for _ in range(N):
        c, d = map(int, input().split())
        T.append((c, d))
    for p in range(360):
        for q in range(-10, 11):
            for r in range(-10, 11):
                S_ = [(a * math.cos(math.radians(p)) - b * math.sin(math.radians(p)) + q, a * math.sin(math.radians(p)) + b * math.cos(math.radians(p)) + r) for a, b in S]
                if S_ == T:
                    print('Yes')
                    return
    print('No')
