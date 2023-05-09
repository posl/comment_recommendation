def print_tiles(N, A, B):
    for i in range(0, N):
        for j in range(0, A):
            for k in range(0, N):
                if (i + j) % 2 == 0:
                    for l in range(0, B):
                        if (k + l) % 2 == 0:
                            print('.', end='')
                        else:
                            print('#', end='')
                else:
                    for l in range(0, B):
                        if (k + l) % 2 == 0:
                            print('#', end='')
                        else:
                            print('.', end='')
            print('')
    return
N, A, B = map(int, input().split())
print_tiles(N, A, B)
