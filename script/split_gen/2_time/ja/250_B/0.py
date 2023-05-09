def main():
    N, A, B = map(int, input().split())
    for i in range(N):
        for j in range(A):
            for k in range(N):
                for l in range(B):
                    if i % 2 == 0:
                        if k % 2 == 0:
                            print('.', end='')
                        else:
                            print('#', end='')
                    else:
                        if k % 2 == 0:
                            print('#', end='')
                        else:
                            print('.', end='')
                print()
        print()
