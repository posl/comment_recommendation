def main():
    from collections import Counter
    N = int(input())
    A = list(map(int, input().split()))
    C = Counter(A)
    S = sorted(C.items(), key=lambda x: x[0])
    T = [0]
    for i in range(len(S)):
        T.append(T[i] + S[i][1])
    for i in range(N):
        print(T[bisect.bisect_left(S, (A[i], 0))] + N - T[bisect.bisect_right(S, (A[i], 10**9))])

if __name__ == '__main__':
    main()