def main():
    N, M = map(int, input().split())
    B = [list(map(int, input().split())) for _ in range(N)]
    for i in range(10**5):
        for j in range(7):
            if i + N <= 10**5 and j + M <= 7:
                A = [[(i+k)*7+j+l for l in range(M)] for k in range(N)]
                if A == B:
                    print('Yes')
                    return
    print('No')

if __name__ == '__main__':
    main()