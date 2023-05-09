def main():
    N, M = map(int, input().split())
    B = [list(map(int, input().split())) for _ in range(N)]
    for i in range(10**4):
        for j in range(7):
            if i + N > 10**4 or j + M > 7:
                break
            A = [[(i + k) * 7 + j + l for l in range(M)] for k in range(N)]
            if A == B:
                print('Yes')
                return
    print('No')
    return

if __name__ == '__main__':
    main()