def matrix_equal():
    h1,w1 = map(int, input().split())
    a = []
    for i in range(h1):
        a.append(list(map(int, input().split())))
    h2,w2 = map(int, input().split())
    b = []
    for i in range(h2):
        b.append(list(map(int, input().split())))
    if h1 < h2 or w1 < w2:
        print("No")
        return
    for i in range(h1):
        for j in range(w1):
            if i+h2 > h1 or j+w2 > w1:
                continue
            if a[i][j] == b[0][0]:
                flag = True
                for k in range(h2):
                    for l in range(w2):
                        if a[i+k][j+l] != b[k][l]:
                            flag = False
                if flag:
                    print("Yes")
                    return
    print("No")

if __name__ == '__main__':
    matrix_equal()