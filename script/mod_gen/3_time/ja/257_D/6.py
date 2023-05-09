def main():
    N = int(input())
    J = [list(map(int,input().split())) for _ in range(N)]
    #print(J)
    ans = 10**9
    for i in range(N):
        S = 0
        for j in range(N):
            if J[i][2]*S >= abs(J[i][0]-J[j][0]) + abs(J[i][1]-J[j][1]):
                continue
            else:
                S += 1
        ans = min(ans,S)
    print(ans)
main()

if __name__ == '__main__':
    main()