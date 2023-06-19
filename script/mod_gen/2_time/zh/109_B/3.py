def shiritori():
    n = int(input())
    w = []
    for i in range(n):
        w.append(input())
    flag = True
    for i in range(1,n):
        if w[i] in w[:i] or w[i-1][-1] != w[i][0]:
            flag = False
            break
    if flag:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    shiritori()