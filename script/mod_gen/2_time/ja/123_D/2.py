def main():
    X, Y, Z, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))
    AB = sorted([a + b for a in A for b in B], reverse=True)[:K]
    ABC = sorted([ab + c for ab in AB for c in C], reverse=True)[:K]
    for abc in ABC:
        print(abc)

if __name__ == '__main__':
    main()