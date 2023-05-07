def main():
    N, A, B = map(int, input().split())
    for i in range(A):
        for j in range(N):
            for k in range(B):
                for l in range(N):
                    if (i + j + k + l) % 2 == 0:
                        print('.', end='')
                    else:
                        print('#', end='')
            print()
