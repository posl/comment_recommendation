def main():
    N, M = map(int, input().split())
    S = list(input().split())
    T = list(input().split())
    express = [False] * N
    for i in range(M):
        express[S.index(T[i])] = True
    for i in range(N):
        if express[i]:
            print("Yes")
        else:
            print("No")

if __name__ == '__main__':
    main()