def main():
    h,w = map(int,input().split())
    matrix = []
    for i in range(h):
        matrix.append(list(map(int,input().split())))
    for i in range(h):
        for j in range(w):
            for k in range(i+1,h):
                for l in range(j+1,w):
                    if matrix[i][j]+matrix[k][l]>matrix[i][l]+matrix[k][j]:
                        print("No")
                        exit()
    print("Yes")
