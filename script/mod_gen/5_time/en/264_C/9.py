def main():
    # Get input here
    h1, w1 = map(int, input().strip().split())
    a = []
    for _ in range(h1):
        a.append(list(map(int, input().strip().split())))
    h2, w2 = map(int, input().strip().split())
    b = []
    for _ in range(h2):
        b.append(list(map(int, input().strip().split())))
    # print(h1, w1, a)
    # print(h2, w2, b)
    # Main logic starts here
    for i in range(h1 - h2 + 1):
        for j in range(w1 - w2 + 1):
            # print(i, j)
            if a[i][j] == b[0][0]:
                flag = 1
                for k in range(h2):
                    for l in range(w2):
                        if a[i + k][j + l] != b[k][l]:
                            flag = 0
                            break
                    if flag == 0:
                        break
                if flag == 1:
                    print("Yes")
                    return
    print("No")

if __name__ == '__main__':
    main()