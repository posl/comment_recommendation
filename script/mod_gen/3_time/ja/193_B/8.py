def main():
    N = int(input())
    P = []
    for i in range(N):
        A, P, X = map(int, input().split())
        if X - A > 0:
            P.append([P, X])
    if len(P) == 0:
        print(-1)
    else:
        print(min(P)[0])

if __name__ == '__main__':
    main()