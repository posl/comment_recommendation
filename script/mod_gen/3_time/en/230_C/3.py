def main():
    N, A, B = map(int, input().split())
    P, Q, R, S = map(int, input().split())
    A -= 1
    B -= 1
    P -= 1
    Q -= 1
    R -= 1
    S -= 1
    print('#' * (S - R + 1))
    for i in range(Q - P):
        if i % 2 == 0:
            print('.' * R + '#' + '.' * (S - R - 1))
        else:
            print('.' * (S - 1) + '#')
    print('#' * (S - R + 1))

if __name__ == '__main__':
    main()