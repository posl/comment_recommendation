def main():
    N = int(input())
    T = []
    K = []
    A = []
    for i in range(N):
        t, k, *a = map(int, input().split())
        T.append(t)
        K.append(k)
        A.append(a)
    time = 0
    for i in range(N-1, -1, -1):
        if T[i] == 0:
            time = max(time, 0)
        else:
            time = max(time, T[i] + time)
    print(time)
main()
