def main():
    # input
    A, B, C, D = map(int, input().split())
    # compute
    cnt = 0
    for i in range(A, B+1):
        if i % C != 0 and i % D != 0:
            cnt += 1
    # output
    print(cnt)
