def main():
    N, A, B = map(int, input().split())
    P, Q, R, S = map(int, input().split())
    for i in range(P, Q+1):
        for j in range(R, S+1):
            if (A <= i <= A+B-1 and R <= j <= S) or (P <= i <= Q and B <= j <= B+A-1):
                print('#', end='')
            else:
                print('.', end='')
        print()
