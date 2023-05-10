def main():
    H, W = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]
    ans = []
    for i in range(H):
        for j in range(W):
            for k in range(i+1, H):
                for l in range(j+1, W):
                    if (A[i][j] + A[k][l] > A[i][l] + A[k][j]):
                        ans.append("No")
                        break
                if (len(ans) > 0):
                    break
            if (len(ans) > 0):
                break
        if (len(ans) > 0):
            break
    if (len(ans) > 0):
        print("No")
    else:
        print("Yes")

if __name__ == '__main__':
    main()