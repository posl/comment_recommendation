def problem263_b():
    N = int(input())
    P = [int(x) for x in input().split()]
    max_gen = 0
    for i in range(N):
        gen = 0
        p = i + 1
        while p != -1:
            gen += 1
            p = P[p-1]
        if gen > max_gen:
            max_gen = gen
    print(max_gen)
