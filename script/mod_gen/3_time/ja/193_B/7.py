def main():
    N = int(input())
    P = []
    for i in range(N):
        A, B, C = map(int, input().split())
        if C > 1:
            P.append([A, B])
    if len(P) == 0:
        print(-1)
        return
    P.sort()
    print(P[0][1])

if __name__ == '__main__':
    main()