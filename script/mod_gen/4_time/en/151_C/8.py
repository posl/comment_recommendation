def main():
    import sys
    import io
    import time
    import pprint
    # sys.stdin = io.StringIO(_INPUT)
    # start_time = time.time()
    # pprint.pprint(sys.stdin.readlines())
    N, M = map(int, sys.stdin.readline().split())
    # print(N, M)
    p = [0] * N
    s = [0] * N
    for i in range(M):
        _p, _s = sys.stdin.readline().split()
        p[int(_p) - 1] += 1
        s[int(_p) - 1] += 1 if _s == 'AC' else 0
    # print(p)
    # print(s)
    correct = 0
    penalty = 0
    for i in range(N):
        if s[i] > 0:
            correct += 1
            penalty += p[i] - 1 if s[i] == 0 else p[i]
    print(correct, penalty)
    # print("elapsed:", time.time() - start_time)

if __name__ == '__main__':
    main()