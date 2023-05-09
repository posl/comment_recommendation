def problems207_b():
    A, B, C, D = map(int, input().split())
    if A <= B * D:
        print(-1)
    else:
        print(-(-A//(B*D-C)))

if __name__ == '__main__':
    problems207_b()