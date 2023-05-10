def main():
    A, B, C, X = map(int, input().split())
    #print(A, B, C, X)
    if A <= X and X <= B:
        print(C / (B - A + 1))
    else:
        print(0)
