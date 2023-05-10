def main():
    # input
    A, B, X = map(int, input().split())
    # compute
    N = 0
    for i in range(1, 10):
        if X >= A*i + B*(len(str(i))):
            N = i
        else:
            break
    # output
    print(N)
