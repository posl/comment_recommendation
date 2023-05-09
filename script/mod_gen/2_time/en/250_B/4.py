def main():
    N, A, B = (int(x) for x in input().split())
    for i in range(A*N):
        if i % A == 0:
            for j in range(B*N):
                if j % B == 0:
                    if (i//A) % 2 == 0:
                        if (j//B) % 2 == 0:
                            print('.', end='')
                        else:
                            print('#', end='')
                    else:
                        if (j//B) % 2 == 0:
                            print('#', end='')
                        else:
                            print('.', end='')
                else:
                    print('.', end='')
        else:
            for j in range(B*N):
                if j % B == 0:
                    if (i//A) % 2 == 0:
                        if (j//B) % 2 == 0:
                            print('#', end='')
                        else:
                            print('.', end='')
                    else:
                        if (j//B) % 2 == 0:
                            print('.', end='')
                        else:
                            print('#', end='')
                else:
                    print('#', end='')
        print()

if __name__ == '__main__':
    main()