def main():
    h1, w1 = map(int, input().split())
    A = []
    for i in range(h1):
        A.append(list(map(int, input().split())))
    h2, w2 = map(int, input().split())
    B = []
    for i in range(h2):
        B.append(list(map(int, input().split())))
    if h1 < h2 or w1 < w2:
        print("No")
        return
    for i in range(h1 - h2 + 1):
        for j in range(w1 - w2 + 1):
            if A[i][j] == B[0][0]:
                flag = True
                for k in range(h2):
                    for l in range(w2):
                        if A[i + k][j + l] != B[k][l]:
                            flag = False
                            break
                    if not flag:
                        break
                if flag:
                    print("Yes")
                    return
    print("No")
main()
