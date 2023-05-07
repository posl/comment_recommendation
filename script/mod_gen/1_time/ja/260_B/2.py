def main():
    N, X, Y, Z = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = [A[i] + B[i] for i in range(N)]
    A = sorted([(A[i], i + 1) for i in range(N)], reverse=True)
    B = sorted([(B[i], i + 1) for i in range(N)], reverse=True)
    C = sorted([(C[i], i + 1) for i in range(N)], reverse=True)
    a, b, c = 0, 0, 0
    ans = set()
    while len(ans) < X:
        ans.add(A[a][1])
        a += 1
    while len(ans) < X + Y:
        ans.add(B[b][1])
        b += 1
    while len(ans) < X + Y + Z:
        ans.add(C[c][1])
        c += 1
    for i in sorted(list(ans)):
        print(i)

if __name__ == '__main__':
    main()