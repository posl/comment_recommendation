def main():
    N, P, Q, R = map(int, input().split())
    A = list(map(int, input().split()))
    if N < 4:
        print("No")
        return
    #前缀和
    S = [0]*(N+1)
    for i in range(N):
        S[i+1] = S[i] + A[i]
    #print(S)
    #从左到右，找到满足条件的y
    y = 1
    while y < N-1:
        if S[y] >= P:
            break
        y += 1
    if y == N-1:
        print("No")
        return
    #从y开始，找到满足条件的z
    z = y + 1
    while z < N-1:
        if S[z] - S[y] >= Q:
            break
        z += 1
    if z == N-1:
        print("No")
        return
    #从z开始，找到满足条件的w
    w = z + 1
    while w < N:
        if S[w] - S[z] >= R:
            break
        w += 1
    if w == N:
        print("No")
        return
    print("Yes")

if __name__ == '__main__':
    main()