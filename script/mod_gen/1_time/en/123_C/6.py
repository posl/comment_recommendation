def main():
    N = int(input())
    A = int(input())
    B = int(input())
    C = int(input())
    D = int(input())
    E = int(input())
    #print(N, A, B, C, D, E)
    min = A
    if min > B:
        min = B
    if min > C:
        min = C
    if min > D:
        min = D
    if min > E:
        min = E
    #print(min)
    if N % min == 0:
        print(N // min + 4)
    else:
        print(N // min + 5)

if __name__ == '__main__':
    main()