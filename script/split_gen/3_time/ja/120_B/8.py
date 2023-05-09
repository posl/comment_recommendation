def main():
    # input
    A, B, K = map(int, input().split())
    # compute
    list = []
    for i in range(1, min(A, B)+1):
        if A%i == 0 and B%i == 0:
            list.append(i)
    # output
    print(list[-K])
