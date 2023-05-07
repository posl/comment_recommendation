def main():
    N = int(input())
    D = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    for i in range(N-2):
        if D[i][0] == D[i][1] and D[i+1][0] == D[i+1][1] and D[i+2][0] == D[i+2][1]:
            ans = 1
            break
    if ans == 1:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()