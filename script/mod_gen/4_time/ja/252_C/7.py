def main():
    N = int(input())
    S = []
    for i in range(N):
        S.append(input())
    #print(N)
    #print(S)
    # ここに書く
    ans = 0
    for i in range(N):
        ans = ans + 10
        for j in range(10):
            if S[i][j] == str((j+1)%10):
                ans = ans - 1
                break
    print(ans)
main()

if __name__ == '__main__':
    main()