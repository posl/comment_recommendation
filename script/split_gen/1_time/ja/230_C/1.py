def main():
    N, A, B = map(int, input().split())
    P, Q, R, S = map(int, input().split())
    for i in range(P, Q+1):
        for j in range(R, S+1):
            if (max(1-A, 1-B) <= i-j <= min(N-A, N-B)) or (max(1-A, B-N) <= i+j <= min(N-A, B-1)):
                print('#', end='')
            else:
                print('.', end='')
        print()
