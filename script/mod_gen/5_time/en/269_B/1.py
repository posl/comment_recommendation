def main():
    input = sys.stdin.readline
    S = [input().rstrip() for _ in range(10)]
    A, B, C, D = 0, 0, 0, 0
    for i in range(10):
        if '#' in S[i]:
            A = i
            break
    for i in range(9, -1, -1):
        if '#' in S[i]:
            B = i
            break
    for i in range(10):
        if '#' in [S[j][i] for j in range(10)]:
            C = i
            break
    for i in range(9, -1, -1):
        if '#' in [S[j][i] for j in range(10)]:
            D = i
            break
    print(A+1, B+1)
    print(C+1, D+1)

if __name__ == '__main__':
    main()