def main():
    n = int(input())
    S = set()
    for i in range(n):
        L = list(map(int, input().split()))
        S.add(tuple(L[1:]))
    print(len(S))

if __name__ == '__main__':
    main()