def main():
    N, A, B = map(int, input().split())
    for i in range(A):
        for j in range(B):
            for k in range(N):
                if (i + j) % 2 == 0:
                    print('.', end='')
                else:
                    print('#', end='')
        print()
