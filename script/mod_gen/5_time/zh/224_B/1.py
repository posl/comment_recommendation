def main():
    h,w = map(int,input().split())
    a = [[int(i) for i in input().split()] for j in range(h)]
    for i in range(h):
        for j in range(w):
            for k in range(i+1,h):
                for l in range(j+1,w):
                    if a[i][j]+a[k][l] > a[i][l]+a[k][j]:
                        print("No")
                        return
    print("Yes")

if __name__ == '__main__':
    main()