def main():
    N = int(input())
    S = [tuple(map(int, input().split())) for _ in range(N)]
    T = [tuple(map(int, input().split())) for _ in range(N)]
    S.sort()
    T.sort()
    for i in range(N):
        x = T[0][0] - S[i][0]
        y = T[0][1] - S[i][1]
        for j in range(N):
            if (S[j][0] + x, S[j][1] + y) not in T:
                break
        else:
            print("Yes")
            break
    else:
        print("No")
main()
