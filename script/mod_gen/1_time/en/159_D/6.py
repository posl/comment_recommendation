def main():
    N = int(input())
    A = [int(x) for x in input().split()]
    C = [0] * N
    for a in A:
        C[a-1] += 1
    S = sum([c*(c-1)//2 for c in C])
    for a in A:
        print(S - (C[a-1]-1))

if __name__ == '__main__':
    main()