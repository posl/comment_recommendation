def main():
    h1,w1 = map(int,input().split())
    a = []
    for i in range(h1):
        a.append(list(map(int,input().split())))
    h2,w2 = map(int,input().split())
    b = []
    for i in range(h2):
        b.append(list(map(int,input().split())))
    for i in range(h1-h2+1):
        for j in range(w1-w2+1):
            if a[i][j] == b[0][0]:
                flag = True
                for k in range(h2):
                    for l in range(w2):
                        if a[i+k][j+l] != b[k][l]:
                            flag = False
                            break
                if flag:
                    print("Yes")
                    return
    print("No")
    return
