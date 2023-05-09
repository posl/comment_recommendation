def main():
    A, B, Q = map(int, input().split())
    S = [int(input()) for _ in range(A)]
    T = [int(input()) for _ in range(B)]
    X = [int(input()) for _ in range(Q)]
    for x in X:
        s1 = 0
        s2 = 0
        t1 = 0
        t2 = 0
        for s in S:
            if s < x:
                s1 = s
            elif s == x:
                s1 = s
                s2 = s
                break
            else:
                s2 = s
                break
        for t in T:
            if t < x:
                t1 = t
            elif t == x:
                t1 = t
                t2 = t
                break
            else:
                t2 = t
                break
        s1_t1 = abs(x-s1) + abs(t1-s1)
        s1_t2 = abs(x-s1) + abs(t2-s1)
        s2_t1 = abs(x-s2) + abs(t1-s2)
        s2_t2 = abs(x-s2) + abs(t2-s2)
        s1_t1_s2_t1 = max(s1_t1, s2_t1)
        s1_t1_s2_t2 = max(s1_t1, s2_t2)
        s1_t2_s2_t1 = max(s1_t2, s2_t1)
        s1_t2_s2_t2 = max(s1_t2, s2_t2)
        print(min(s1_t1_s2_t1, s1_t1_s2_t2, s1_t2_s2_t1, s1_t2_s2_t2))
