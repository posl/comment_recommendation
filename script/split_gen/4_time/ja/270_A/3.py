def main():
    # input
    A, B = map(int, input().split())
    # compute
    S = A + B
    if S >= 15 and B >= 8:
        result = 1
    elif S >= 10 and B >= 3:
        result = 2
    elif S >= 3:
        result = 3
    else:
        result = 4
    # output
    print(result)
