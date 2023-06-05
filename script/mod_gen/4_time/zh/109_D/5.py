def main():
    h,w = map(int,input().split())
    a = [list(map(int,input().split())) for _ in range(h)]
    ans = []
    for i in range(h):
        for j in range(w):
            if i%2 == 0:
                if a[i][j]%2 == 1:
                    if j != w-1:
                        a[i][j] -= 1
                        a[i][j+1] += 1
                        ans.append([i+1,j+1,i+1,j+2])
                    elif i != h-1:
                        a[i][j] -= 1
                        a[i+1][j] += 1
                        ans.append([i+1,j+1,i+2,j+1])
            else:
                if a[i][w-1-j]%2 == 1:
                    if j != w-1:
                        a[i][w-1-j] -= 1
                        a[i][w-1-j-1] += 1
                        ans.append([i+1,w-j,i+1,w-j-1])
                    elif i != h-1:
                        a[i][w-1-j] -= 1
                        a[i+1][w-1-j] += 1
                        ans.append([i+1,w-j,i+2,w-j])
    print(len(ans))
    for i in range(len(ans)):
        print(ans[i][0],ans[i][1],ans[i][2],ans[i][3])

if __name__ == '__main__':
    main()