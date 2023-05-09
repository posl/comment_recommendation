def main():
    N, A, B = map(int, input().split())
    P, Q, R, S = map(int, input().split())
    for i in range(P, Q+1):
        for j in range(R, S+1):
            if (i+j) % 2 == 0 and N-A >= i-A and N-B >= j-B:
                print("#", end="")
            elif (i+j) % 2 == 1 and N-A >= i-A and B-1 >= j-B:
                print("#", end="")
            else:
                print(".", end="")
        print()
