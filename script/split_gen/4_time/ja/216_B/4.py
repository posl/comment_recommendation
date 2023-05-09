def main():
    N = int(input())
    S_T = [input().split() for i in range(N)]
    for i in range(N):
        for j in range(i+1,N):
            if S_T[i][0] == S_T[j][0] and S_T[i][1] == S_T[j][1]:
                print("Yes")
                return
    print("No")
