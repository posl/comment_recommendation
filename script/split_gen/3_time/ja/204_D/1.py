def main():
    N = int(input())
    T = list(map(int, input().split()))
    T.sort()
    if N == 1:
        print(T[0])
    elif N == 2:
        print(max(T[0], T[1]))
    else:
        T1 = T[0]
        T2 = T[1]
        for i in range(2, N):
            if T1 < T2:
                T1 += T[i]
            else:
                T2 += T[i]
        print(max(T1, T2))
