def problems207_b():
    A, B, C, D = map(int, input().split())
    if A <= B * D:
        print(-1)
    else:
        print(-(-A//(B*D-C)))
