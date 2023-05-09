def main():
    import sys
    import numpy as np
    N, M = map(int, sys.stdin.readline().split())
    if M == 0:
        print(3**N)
        return
    edges = np.zeros((N, N), dtype=np.int64)
    for i in range(M):
        A, B = map(int, sys.stdin.readline().split())
        edges[A - 1][B - 1] = 1
        edges[B - 1][A - 1] = 1
    ans = 0
    for i in range(3**N):
        flag = True
        for j in range(N):
            for k in range(N):
                if edges[j][k] == 1 and (i // 3**j) % 3 == (i // 3**k) % 3:
                    flag = False
                    break
            if not flag:
                break
        if flag:
            ans += 1
    print(ans)
