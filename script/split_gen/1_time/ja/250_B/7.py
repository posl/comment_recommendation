def main():
    N, A, B = map(int, input().split())
    for i in range(A):
        for j in range(B):
            if (i + j) % 2 == 0:
                for k in range(N):
                    print('.' * N, end='')
            else:
                for k in range(N):
                    print('#' * N, end='')
        print('')
