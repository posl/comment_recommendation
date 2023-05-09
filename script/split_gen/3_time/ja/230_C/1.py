def main():
    N, A, B = map(int, input().split())
    P, Q, R, S = map(int, input().split())
    for i in range(P, Q+1):
        for j in range(R, S+1):
            if (i + j - A - B) % 2 == 0 and (i - A) * (i - A) + (j - B) * (j - B) <= N * N:
                print('#', end='')
            else:
                print('.', end='')
        print()
