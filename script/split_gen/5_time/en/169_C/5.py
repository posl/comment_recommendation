def main():
    # input
    A, B = input().split()
    # compute
    A = int(A)
    B = int(B.replace('.', ''))
    # output
    print(A*B//100)
