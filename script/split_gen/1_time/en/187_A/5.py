def main():
    # input
    A, B = map(int, input().split())
    # compute
    # output
    print(max(sum(map(int, str(A))), sum(map(int, str(B)))))
