def main():
    N = int(input())
    L = [0] * N
    R = [0] * N
    for i in range(N):
        L[i],R[i] = map(int,input().split())
    S = sorted(zip(L,R))
    ans = []
    now = S[0]
    for i in range(1,N):
        if now[1] >= S[i][0]:
            now = (now[0],max(now[1],S[i][1]))
        else:
            ans.append(now)
            now = S[i]
    ans.append(now)
    for i in ans:
        print(i[0],i[1])

if __name__ == '__main__':
    main()